from sqlalchemy import Column, ForeignKey, Integer
from sqlmodel import Field as ModelField

from app.model.base_model import CustomBaseModel


class BucketItem(CustomBaseModel, table=True):
    bucket_id: int = ModelField(sa_column=Column(Integer, ForeignKey("bucket.id", ondelete="NO ACTION")), nullable=False)
    tool_id: int = ModelField(sa_column=Column(Integer, ForeignKey("tool.id", ondelete="NO ACTION")), nullable=False)
