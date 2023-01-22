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
    profile_image_url: str = ModelField(default="", nullable=False)
    user_token: str = ModelField(nullable=False)
    is_verified: bool = ModelField(default=False, nullable=False)
    is_activated: bool = ModelField(default=True, nullable=False)
    is_superuser: bool = ModelField(default=False, nullable=False)


class UserDto:
    class Base(BaseModel):
        email: str = Field(..., description="user email", example="jujumilk3@gmail.com")
        nickname: str = Field(..., description="user nickname", example="gyudoza")
        user_token: str = Field(..., description="user token", example="test_user_token")
        profile_image_url: str = Field(
            default="", description="user profile image url", example="https://via.placeholder.com/150"
        )


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
        email: str = Field(nullable=False, example="test@test.com")
        password: str = Field(nullable=False, example="test1234")

    class SignInResponse(BaseModel):
        access_token: str
        expiration: int
        user_info: UserDto.Base
