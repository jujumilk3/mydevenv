from sqlmodel import Field as ModelField

from app.model.base_model import CustomBaseModel


class Bucket(CustomBaseModel, table=True):
    name: str = ModelField(default="", nullable=False)
    user_token: str = ModelField(nullable=False)
