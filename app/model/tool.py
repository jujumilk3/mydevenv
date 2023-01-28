from sqlmodel import Field as ModelField

from app.model.base_model import CustomBaseModel


class Tool(CustomBaseModel, table=True):
    display_name: str = ModelField(default="", nullable=False)
    manage_name: str = ModelField(default="", nullable=False)
    image_url: str = ModelField(default="", nullable=False)
    is_open_source: bool = ModelField(default=False, nullable=False)
    site_url: str = ModelField(default="", nullable=False)
    github_url: str = ModelField(default="", nullable=False)


class ToolTag(CustomBaseModel, table=True):
    name: str = ModelField(default="", nullable=False)
    description: str = ModelField(default="", nullable=False)


class ToolToolRelation(CustomBaseModel, table=True):
    source_tool_id: int = ModelField(nullable=False)
    reference_tool_id: int = ModelField(nullable=False)


class ToolTagRelation(CustomBaseModel, table=True):
    tool_id: int = ModelField(nullable=False)
    tag_id: int = ModelField(nullable=False)
