from pydantic import Field
from sqlmodel import Field as ModelField

from app.core.constant import TagCategoryType
from app.model.base_model import AllOptional, CustomBaseModel, CustomBaseModelDto, ModelBaseInfoDto


class Tag(CustomBaseModel, table=True):
    user_token: str = ModelField(default="", nullable=False)

    name: str = ModelField(default="", nullable=False)
    description: str = ModelField(default="", nullable=False)
    category: TagCategoryType = ModelField(default="", nullable=False)


class TagDto:
    class Base(CustomBaseModelDto):
        name: str = Field(..., description="tag name", example="test tag")
        description: str = Field(..., description="tag description", example="test tag")
        category: TagCategoryType | None = Field(None, description="tag category", example="tool")

    class WithBaseInfo(ModelBaseInfoDto, Base, metaclass=AllOptional):
        user_token: str = Field(..., description="user token", example="test_user_token")

    class WithAdditionalInfo(WithBaseInfo, metaclass=AllOptional):
        like_num: int = Field(default=0, example=0)
        is_liked: bool = Field(default=False, example=False)

    class Upsert(Base, metaclass=AllOptional): ...

    class UpsertWithUserToken(Base, metaclass=AllOptional):
        user_token: str
