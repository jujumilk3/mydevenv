from collections.abc import Callable
from contextlib import AbstractContextManager

from sqlalchemy.ext.asyncio import AsyncSession

from app.model.tool import Tool, ToolTag, ToolTagRelation, ToolToolRelation
from app.repository.base_repository import BaseRepository


class ToolRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Tool)


class ToolTagRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]):
        self.session_factory = session_factory
        super().__init__(session_factory, ToolTag)


class ToolToolRelationRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]):
        self.session_factory = session_factory
        super().__init__(session_factory, ToolToolRelation)


class ToolTagRelationRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]):
        self.session_factory = session_factory
        super().__init__(session_factory, ToolTagRelation)
