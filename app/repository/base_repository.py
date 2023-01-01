from collections.abc import Callable
from contextlib import AbstractContextManager

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exception import DuplicatedError, NotFoundError


class BaseRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]], model) -> None:
        self.session_factory = session_factory
        self._model = model
        self._model_name = self._model.__name__

    async def select_by_id(self, model_id: int):
        async with self.session_factory() as session:
            query = select(self._model).where(self._model.id == model_id)
            query_result = await session.execute(query)
            found_model = query_result.scalar()
            if not found_model:
                raise NotFoundError(detail=f"not found model name: {self._model_name}, requested id: {model_id}")
            return found_model

    async def select_by_ids(self, model_ids: list[int]):
        async with self.session_factory() as session:
            query = select(self._model).where(self._model.id.in_(model_ids))
            query_result = await session.execute(query)
            found_model_list = query_result.scalars().all()
            return found_model_list

    async def insert(self, dto):
        async with self.session_factory() as session:
            query = self._model(**dto.dict())
            try:
                session.add(query)
                await session.commit()
                await session.refresh(query)
            except IntegrityError as e:
                raise DuplicatedError(detail=str(e.orig)) from e
            return query

    async def update(self, model_id: int, dto: BaseModel):
        async with self.session_factory() as session:
            found_model = await self.select_by_id(model_id)
            for key, value in dto.dict().items():
                if value is None:
                    continue
                setattr(found_model, key, value)
            await session.commit()
            return found_model

    async def upsert(self, model_id: int, dto: BaseModel):
        try:
            await self.select_by_id(model_id)
        except NotFoundError:
            return await self.insert(dto)
        return self.update(model_id=model_id, dto=dto)

    async def delete_by_id(self, model_id: int):
        async with self.session_factory() as session:
            found_model = await self.select_by_id(model_id)
            if not found_model:
                raise NotFoundError(detail=f"not found model name: {self._model_name}, requested id: {model_id}")
            await session.delete(found_model)
            await session.commit()
