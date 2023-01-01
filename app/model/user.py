from pydantic import BaseModel
from sqlalchemy.sql.schema import UniqueConstraint
from sqlmodel import Field

from app.model.base_model import CustomBaseModel


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


class AuthDto:
    class JWTPayload(BaseModel):
        email: str
        nickname: str
        user_token: str
        is_verified: bool
        is_activated: bool

        class Config:
            orm_mode = True

    class SignUp(BaseModel):
        email: str
        password: str
        nickname: str

    class SignIn(BaseModel):
        email: str
        password: str


class UserDto:
    class Base(BaseModel):
        email: str
        password: str
        nickname: str
        user_token: str
        is_verified: bool
        is_activated: bool
