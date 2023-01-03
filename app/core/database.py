from asyncio import current_task
from typing import Any
from sqlmodel import SQLModel

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, create_async_engine
from sqlalchemy.ext.declarative import as_declarative, declarative_base, declared_attr

from app.core.config import configs


@as_declarative()
class BaseModel:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


Base = declarative_base()


class Database:
    def __init__(self, db_url: str, sync_db_url: str) -> None:
        # db engine
        self.engine = create_async_engine(db_url)
        self.sync_engine = create_engine(sync_db_url)

        # db session factory
        self._session_factory = async_scoped_session(
            session_factory=orm.sessionmaker(
                bind=self.engine,
                class_=AsyncSession,
                autocommit=False,
                autoflush=False,
            ),
            scopefunc=current_task,
        )

        if configs.ENV == "dev":
            self.create_all()

    @property
    def session_factory(self):
        return self._session_factory

    def create_all(self):
        SQLModel.metadata.create_all(self.sync_engine)
