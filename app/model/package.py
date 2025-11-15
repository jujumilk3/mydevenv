from pydantic import Field
from sqlmodel import Field as ModelField

from app.model.base_model import AllOptional, CustomBaseModel, CustomBaseModelDto, ModelBaseInfoDto


class Package(CustomBaseModel, table=True):
    """Installable package (npm, pip, brew, apt, etc.)"""

    name: str = ModelField(default="", nullable=False)
    description: str = ModelField(default="", nullable=False)
    package_manager: str = ModelField(default="", nullable=False)  # npm, pip, brew, apt, cargo, etc.
    version: str = ModelField(default="latest", nullable=False)
    install_command: str = ModelField(default="", nullable=False)  # custom install command if needed
    is_global: bool = ModelField(default=False, nullable=False)  # global or local installation
    platform: str = ModelField(default="all", nullable=False)  # linux, macos, windows, all


class BucketPackage(CustomBaseModel, table=True):
    """Relation between Bucket and Package"""

    bucket_id: int = ModelField(nullable=False)
    package_id: int = ModelField(nullable=False)
    is_required: bool = ModelField(default=True, nullable=False)  # required or optional


class PackageDto:
    class Base(CustomBaseModelDto):
        name: str = Field(..., description="package name", example="fastapi")
        description: str = Field(..., description="package description", example="Modern web framework")
        package_manager: str = Field(..., description="package manager", example="pip")
        version: str = Field(default="latest", description="package version", example="0.100.0")
        install_command: str = Field(
            default="", description="custom install command", example="pip install fastapi"
        )
        is_global: bool = Field(default=False, description="global installation", example=False)
        platform: str = Field(default="all", description="target platform", example="all")

    class Upsert(Base, metaclass=AllOptional): ...

    class WithBaseInfo(ModelBaseInfoDto, Base, metaclass=AllOptional): ...

    class WithAdditionalInfo(WithBaseInfo, metaclass=AllOptional):
        is_required: bool = Field(default=True, description="required package", example=True)


class BucketPackageDto:
    class Base(CustomBaseModelDto):
        bucket_id: int = Field(..., description="bucket id", example=1)
        package_id: int = Field(..., description="package id", example=1)
        is_required: bool = Field(default=True, description="required package", example=True)

    class Upsert(Base, metaclass=AllOptional): ...
