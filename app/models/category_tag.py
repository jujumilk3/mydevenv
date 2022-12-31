from sqlmodel import Field

from app.models.base_model import CustomBaseModel


class CategoryTag(CustomBaseModel, table=True):
    display_name: str = Field(default="", nullable=False)
    manage_name: str = Field(default="", nullable=False)
    image_url: str = Field(default="", nullable=False)

