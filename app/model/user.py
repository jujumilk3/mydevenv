from pydantic import BaseModel, Field
from sqlalchemy.sql.schema import UniqueConstraint
from sqlmodel import Field as ModelField

from app.model.base_model import CustomBaseModel


class User(CustomBaseModel, table=True):
    __table_args__ = (
        UniqueConstraint("email", name="uq_user_email"),
        UniqueConstraint("user_token", name="uq_user_token"),
        UniqueConstraint("nickname", name="uq_user_nickname"),
    )

    email: str = ModelField(nullable=False)
    password: str = ModelField(nullable=False)
    nickname: str = ModelField(nullable=False)
    user_token: str = ModelField(nullable=False)
    is_verified: bool = ModelField(default=False, nullable=False)
    is_activated: bool = ModelField(default=True, nullable=False)
    is_superuser: bool = ModelField(default=False, nullable=False)


class UserDto:
    class Base(BaseModel):
        email: str
        nickname: str
        user_token: str


class AuthDto:
    class Payload(BaseModel):
        email: str
        nickname: str
        user_token: str

    class JWTPayload(BaseModel):
        email: str
        nickname: str
        user_token: str
        access_token: str
        expiration: int

        class Config:
            orm_mode = True

    class SignUp(BaseModel):
        email: str = Field(nullable=False, example="test@test.com")
        password: str = Field(nullable=False, example="test1234")
        nickname: str = Field(nullable=False, example="testnickname")

    class SignIn(BaseModel):
        email: str
        password: str

    class SignInResponse(BaseModel):
        access_token: str
        expiration: int
        user_info: UserDto.Base
