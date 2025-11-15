from pydantic import Field
from sqlmodel import Field as ModelField

from app.model.base_model import AllOptional, CustomBaseModel, CustomBaseModelDto, ModelBaseInfoDto


class ConfigFile(CustomBaseModel, table=True):
    """Configuration file template"""

    name: str = ModelField(default="", nullable=False)
    description: str = ModelField(default="", nullable=False)
    file_path: str = ModelField(default="", nullable=False)  # relative path like .gitconfig, ~/.bashrc
    content: str = ModelField(default="", nullable=False)  # file content
    file_type: str = ModelField(default="text", nullable=False)  # text, json, yaml, toml, etc.
    platform: str = ModelField(default="all", nullable=False)  # linux, macos, windows, all


class BucketConfigFile(CustomBaseModel, table=True):
    """Relation between Bucket and ConfigFile"""

    bucket_id: int = ModelField(nullable=False)
    config_file_id: int = ModelField(nullable=False)
    is_required: bool = ModelField(default=True, nullable=False)


class ConfigFileDto:
    class Base(CustomBaseModelDto):
        name: str = Field(..., description="config file name", example=".gitconfig")
        description: str = Field(..., description="config file description", example="Git configuration")
        file_path: str = Field(..., description="file path", example="~/.gitconfig")
        content: str = Field(..., description="file content", example="[user]\n  name = John Doe")
        file_type: str = Field(default="text", description="file type", example="text")
        platform: str = Field(default="all", description="target platform", example="all")

    class Upsert(Base, metaclass=AllOptional): ...

    class WithBaseInfo(ModelBaseInfoDto, Base, metaclass=AllOptional): ...

    class WithAdditionalInfo(WithBaseInfo, metaclass=AllOptional):
        is_required: bool = Field(default=True, description="required file", example=True)


class BucketConfigFileDto:
    class Base(CustomBaseModelDto):
        bucket_id: int = Field(..., description="bucket id", example=1)
        config_file_id: int = Field(..., description="config file id", example=1)
        is_required: bool = Field(default=True, description="required file", example=True)

    class Upsert(Base, metaclass=AllOptional): ...
