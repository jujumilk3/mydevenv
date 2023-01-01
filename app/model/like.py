from sqlmodel import Field

from app.core.constant import ContentType
from app.model.base_model import CustomBaseModel


class Like(CustomBaseModel, table=True):
    user_token: str = Field(nullable=False)
    content_id: int = Field(nullable=False)
    content_type: ContentType = Field(nullable=False)
