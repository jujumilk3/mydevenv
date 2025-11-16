from pydantic import Field
from sqlmodel import Field as ModelField

from app.model.base_model import AllOptional, CustomBaseModel, CustomBaseModelDto, ModelBaseInfoDto


class Environment(CustomBaseModel, table=True):
    """Environment variable"""

    key: str = ModelField(default="", nullable=False)
    value: str = ModelField(default="", nullable=False)
    description: str = ModelField(default="", nullable=False)
    is_secret: bool = ModelField(default=False, nullable=False)  # whether to mask the value
    platform: str = ModelField(default="all", nullable=False)  # linux, macos, windows, all


class BucketEnvironment(CustomBaseModel, table=True):
    """Relation between Bucket and Environment"""

    bucket_id: int = ModelField(nullable=False)
    environment_id: int = ModelField(nullable=False)
    is_required: bool = ModelField(default=True, nullable=False)


class EnvironmentDto:
    class Base(CustomBaseModelDto):
        key: str = Field(..., description="environment variable key", example="NODE_ENV")
        value: str = Field(..., description="environment variable value", example="development")
        description: str = Field(default="", description="environment variable description", example="Node environment")
        is_secret: bool = Field(default=False, description="secret variable", example=False)
        platform: str = Field(default="all", description="target platform", example="all")

    class Upsert(Base, metaclass=AllOptional): ...

    class WithBaseInfo(ModelBaseInfoDto, Base, metaclass=AllOptional): ...

    class WithAdditionalInfo(WithBaseInfo, metaclass=AllOptional):
        is_required: bool = Field(default=True, description="required variable", example=True)


class BucketEnvironmentDto:
    class Base(CustomBaseModelDto):
        bucket_id: int = Field(..., description="bucket id", example=1)
        environment_id: int = Field(..., description="environment id", example=1)
        is_required: bool = Field(default=True, description="required variable", example=True)

    class Upsert(Base, metaclass=AllOptional): ...
