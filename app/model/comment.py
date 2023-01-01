from sqlmodel import Column, Field

from app.core.constant import ContentType
from app.model.base_model import CustomBaseModel, JsonType


class Comment(CustomBaseModel, table=True):
    user_token: str = Field(nullable=False)
    comment: str = Field(default="", nullable=False)
    mention_tokens: list[str] = Field(sa_column=Column(JsonType), nullable=False)
    parent_comment_id: int = Field(default=None, nullable=True)

    content_id: int = Field(nullable=False)
    content_type: ContentType = Field(nullable=False)
