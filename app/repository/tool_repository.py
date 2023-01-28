from collections.abc import Callable
from contextlib import AbstractContextManager

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.tool import Tool, ToolTagRelation, ToolToolRelation
from app.repository.base_repository import BaseRepository


class ToolRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Tool)

    async def select_by_name(self, name: str) -> Tool:
        async with self.session_factory() as session:
            query = select(Tool).filter(Tool.name == name)
            query_result = await session.execute(query)
            found_tool = query_result.scalar()
            return found_tool

    async def select_by_names(self, names: list[str]) -> list[Tool]:
        async with self.session_factory() as session:
            query = select(Tool).filter(Tool.name.in_(names))
            query_result = await session.execute(query)
            found_tools = query_result.scalars().all()
            return found_tools


class ToolToolRelationRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]):
        self.session_factory = session_factory
        super().__init__(session_factory, ToolToolRelation)

    async def insert_with_source_tool_id_target_tool_id(self, source_tool_id: int, target_tool_id: int):
        async with self.session_factory() as session:
            tool_tool_relation = ToolToolRelation(source_tool_id=source_tool_id, target_tool_id=target_tool_id)
            session.add(tool_tool_relation)
            await session.commit()
            await session.refresh(tool_tool_relation)
            return tool_tool_relation


class ToolTagRelationRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]):
        self.session_factory = session_factory
        super().__init__(session_factory, ToolTagRelation)

    async def insert_with_tool_id_tag_id(self, tool_id: int, tag_id: int):
        async with self.session_factory() as session:
            tool_tag_relation = ToolTagRelation(tool_id=tool_id, tag_id=tag_id)
            session.add(tool_tag_relation)
            await session.commit()
            await session.refresh(tool_tag_relation)
            return tool_tag_relation
