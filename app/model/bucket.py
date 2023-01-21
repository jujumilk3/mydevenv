from sqlmodel import Field as ModelField

from app.model.base_model import CustomBaseModel, AllOptional, ModelBaseInfoDto
from pydantic import BaseModel, Field

from app.model.user import UserDto


class Bucket(CustomBaseModel, table=True):
    name: str = ModelField(default="", nullable=False)
    path: str = ModelField(default="", nullable=False)
    description: str = ModelField(default="", nullable=False)
    memo: str = ModelField(default="", nullable=False)
    user_token: str = ModelField(nullable=False)


class BucketDto:
    class Base(BaseModel):
        name: str = Field(default="", nullable=False, example="local dev for python")
        path: str = Field(default="", nullable=False, example="local-dev-for-python")
        description: str = Field(default="", nullable=False, example="local dev for python")
        memo: str = Field(default="", nullable=False, example="local dev for python")

        class Config:
            orm_mode = True

    class WithBaseInfo(ModelBaseInfoDto, Base, metaclass=AllOptional):
        user_token: str = Field(nullable=False, example="test_user_token")

    class WithAdditionalInfo(WithBaseInfo, metaclass=AllOptional):
        like_num: int = Field(default=0, example=0)
        is_liked: bool = Field(default=False, example=False)
        user_info: UserDto.Base = Field(default=None, example=None)

    class Upsert(Base, metaclass=AllOptional):
        ...
