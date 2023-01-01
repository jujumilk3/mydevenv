from collections.abc import Callable
from contextlib import AbstractContextManager

from sqlalchemy.ext.asyncio import AsyncSession

from app.model.like import Like
from app.repository.base_repository import BaseRepository


class LikeRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Like)
