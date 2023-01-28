from collections.abc import Callable
from contextlib import AbstractContextManager

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.tag import Tag
from app.repository.base_repository import BaseRepository


class TagRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Tag)

    async def select_by_name(self, name: str) -> Tag:
        async with self.session_factory() as session:
            query = select(Tag).filter(Tag.name == name)
            query_result = await session.execute(query)
            found_tag = query_result.scalar()
            return found_tag

    async def select_by_names(self, names: list[str]) -> list[Tag]:
        async with self.session_factory() as session:
            query = select(Tag).filter(Tag.name.in_(names))
            query_result = await session.execute(query)
            found_tags = query_result.scalars().all()
            return found_tags
