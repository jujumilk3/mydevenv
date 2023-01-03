from sqlalchemy import Column, ForeignKey, Integer
from sqlmodel import Field as ModelField
from app.model.base_model import CustomBaseModel


class Tool(CustomBaseModel, table=True):
    display_name: str = ModelField(default="", nullable=False)
    manage_name: str = ModelField(default="", nullable=False)
    image_url: str = ModelField(default="", nullable=False)
    category_id: int = ModelField(sa_column=Column(Integer, ForeignKey("category.id", ondelete="NO ACTION")), nullable=False)
