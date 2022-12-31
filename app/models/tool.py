from sqlalchemy import Column, ForeignKey, Integer
from sqlmodel import Field

from app.models.base_model import CustomBaseModel


class Tool(CustomBaseModel, table=True):
    display_name: str = Field(default="", nullable=False)
    manage_name: str = Field(default="", nullable=False)
    image_url: str = Field(default="", nullable=False)
    category_tag_id: int = Field(sa_column=Column(Integer, ForeignKey("category_tag.id", ondelete="NO ACTION")), nullable=False)
