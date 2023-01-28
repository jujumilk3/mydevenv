from pydantic import Field
from sqlmodel import Field as ModelField

from app.core.constant import TagCategoryType
from app.model.base_model import CustomBaseModel, CustomBaseModelDto, AllOptional


class Tag(CustomBaseModel, table=True):
    name: str = ModelField(default="", nullable=False)
    description: str = ModelField(default="", nullable=False)
    user_token: str = ModelField(default="", nullable=False)
    category: TagCategoryType = ModelField(default="", nullable=False)


class TagDto:
    class Base(CustomBaseModelDto):
        name: str = Field(..., description="tag name", example="test tag")
        description: str = Field(..., description="tag description", example="test tag")
        user_token: str = Field(..., description="user token", example="test_user_token")
        category: TagCategoryType = Field(..., description="tag category", example="tool")

    class Upsert(Base, metaclass=AllOptional):
        ...

    class UpsertWithUserToken(Base, metaclass=AllOptional):
        user_token: str
