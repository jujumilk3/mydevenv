from pydantic import Field
from sqlmodel import Field as ModelField

from app.model.base_model import AllOptional, CustomBaseModel, CustomBaseModelDto
from app.model.tag import TagDto


class Tool(CustomBaseModel, table=True):
    name: str = ModelField(default="", nullable=False)
    description: str = ModelField(default="", nullable=False)
    image_url: str = ModelField(default="", nullable=False)
    is_open_source: bool = ModelField(default=False, nullable=False)
    site_url: str = ModelField(default="", nullable=False)
    github_url: str = ModelField(default="", nullable=False)


class ToolToolRelation(CustomBaseModel, table=True):
    source_tool_id: int = ModelField(nullable=False)
    reference_tool_id: int = ModelField(nullable=False)


class ToolTagRelation(CustomBaseModel, table=True):
    tool_id: int = ModelField(nullable=False)
    tag_id: int = ModelField(nullable=False)


class ToolDto:
    class Base(CustomBaseModelDto):
        name: str = Field(..., description="tool name", example="test_tool")
        description: str = Field(..., description="tool description", example="test_tool")
        image_url: str = Field(..., description="tool image url", example="https://via.placeholder.com/150")
        is_open_source: bool = Field(..., description="tool is open source", example=True)
        site_url: str = Field(..., description="tool site url", example="https://github.com")
        github_url: str = Field(..., description="tool github url", example="https://github.com/jujumilk3/mydevenv")

    class Upsert(Base, metaclass=AllOptional):
        tool_ids: list[int] | None = Field(None, description="tool ids", example=[1, 2, 3])
        tag_ids: list[int] | None = Field(None, description="tool tag ids", example=[1, 2, 3])

    class WithAdditionalInfo(Base, metaclass=AllOptional):
        tools: list["ToolDto.WithAdditionalInfo"] | None = Field(None, description="tools", example=[])
        tags: list[TagDto.WithAdditionalInfo] | None = Field(None, description="tags", example=[])
        like_num: int = Field(default=0, example=0)
        is_liked: bool = Field(default=False, example=False)
