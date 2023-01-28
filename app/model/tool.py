from pydantic import Field
from sqlmodel import Field as ModelField

from app.model.base_model import AllOptional, CustomBaseModel, CustomBaseModelDto


class Tool(CustomBaseModel, table=True):
    display_name: str = ModelField(default="", nullable=False)
    manage_name: str = ModelField(default="", nullable=False)
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
        display_name: str = Field(..., description="tool display name", example="test tool")
        manage_name: str = Field(..., description="tool manage name", example="test_tool")
        image_url: str = Field(..., description="tool image url", example="https://via.placeholder.com/150")
        is_open_source: bool = Field(..., description="tool is open source", example=True)
        site_url: str = Field(..., description="tool site url", example="https://github.com")
        github_url: str = Field(..., description="tool github url", example="https://github.com/jujumilk3/mydevenv")

    class Upsert(Base, metaclass=AllOptional):
        tool_ids: list[int] = Field(..., description="tool ids", example=[1, 2, 3])
        tool_tag_ids: list[int] = Field(..., description="tool tag ids", example=[1, 2, 3])
