from pydantic import BaseModel, Field
from sqlmodel import Field as ModelField

from app.model.base_model import AllOptional, CustomBaseModel, ModelBaseInfoDto, CustomBaseModelDto
from app.model.user import UserDto


class Bucket(CustomBaseModel, table=True):
    user_token: str = ModelField(nullable=False)

    name: str = ModelField(default="", nullable=False)
    path: str = ModelField(default="", nullable=False)
    description: str = ModelField(default="", nullable=False)
    memo: str = ModelField(default="", nullable=False)
    is_published: bool = ModelField(default=True, nullable=False)


class BucketDto:
    class Base(CustomBaseModelDto):
        name: str = Field(default="", nullable=False, example="local dev for python")
        path: str = Field(default="", nullable=False, example="local-dev-for-python")
        description: str = Field(default="", nullable=False, example="local dev for python")
        memo: str = Field(default="", nullable=False, example="local dev for python")
        is_published: bool = Field(default=True, nullable=False, example=True)

    class WithBaseInfo(ModelBaseInfoDto, Base, metaclass=AllOptional):
        user_token: str = Field(nullable=False, example="test_user_token")

    class WithAdditionalInfo(WithBaseInfo, metaclass=AllOptional):
        like_num: int = Field(default=0, example=0)
        is_liked: bool = Field(default=False, example=False)
        user_info: UserDto.Base = Field(default=None, example=None)
        is_published: bool = Field(default=True, nullable=False, example=True)

    class Upsert(Base, metaclass=AllOptional):
        ...

    class UpsertWithUserToken(Base, metaclass=AllOptional):
        user_token: str
