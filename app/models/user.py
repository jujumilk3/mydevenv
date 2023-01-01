from pydantic import BaseModel
from sqlalchemy.sql.schema import UniqueConstraint
from sqlmodel import Field

from app.models.base_model import CustomBaseModel


class User(CustomBaseModel, table=True):
    __table_args__ = (
        UniqueConstraint("email", name="uq_user_email"),
        UniqueConstraint("user_token", name="uq_user_token"),
        UniqueConstraint("nickname", name="uq_user_nickname"),
    )

    email: str = Field(nullable=False)
    password: str = Field(nullable=False)
    nickname: str = Field(nullable=False)
    user_token: str = Field(nullable=False)
    is_verified: bool = Field(default=False, nullable=False)
    is_activated: bool = Field(default=False, nullable=False)


class JWTPayload(BaseModel):
    user_token: str
    is_authenticated: bool
    is_verified: bool
    channel: str
    exp: int

    class Config:
        orm_mode = True
