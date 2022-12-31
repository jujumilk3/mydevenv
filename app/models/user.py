from sqlalchemy.sql.schema import UniqueConstraint
from sqlmodel import Field

from app.models.base_model import CustomBaseModel


class User(CustomBaseModel, table=True):
    __table_args__ = (
        UniqueConstraint("email", name="uq_user_email"),
        UniqueConstraint("user_token", name="uq_user_token"),
        UniqueConstraint("nickname", name="uq_user_nickname"),
    )

    email: str = Field(nullable=False)
    nickname: str = Field(nullable=False)
    user_token: str = Field(nullable=False)
    verified: bool = Field(default=False, nullable=False)
