from sqlmodel import Field

from app.core.constant import CategoryGroup
from app.model.base_model import CustomBaseModel


class Category(CustomBaseModel, table=True):
    display_name: str = Field(default="", nullable=False)
    manage_name: str = Field(default="", nullable=False)
    image_url: str = Field(default="", nullable=False)
    group: CategoryGroup = Field(default="", nullable=False)
