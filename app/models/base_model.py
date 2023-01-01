import json
from datetime import datetime

from sqlmodel import Column, DateTime, Field, SQLModel, String, TypeDecorator, func


class CustomBaseModel(SQLModel):
    id: int = Field(primary_key=True)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now()))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class JsonType(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        if not value:
            return None
        if isinstance(value, str):
            return json.dumps(value)
        else:
            return value

    def process_result_value(self, value, dialect):
        if not value:
            return None
        if isinstance(value, str):
            return json.loads(value)
        else:
            return value

    def copy(self):
        return JsonType(self.impl.length)
