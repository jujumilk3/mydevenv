from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from app.model.tool import Tool
from app.repository.base_repository import BaseRepository


class ToolRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Tool)
