from typing import TYPE_CHECKING

from pydantic import Field
from sqlmodel import Field as ModelField

from app.model.base_model import AllOptional, CustomBaseModel, CustomBaseModelDto, ModelBaseInfoDto
from app.model.user import UserDto

if TYPE_CHECKING:
    from app.model.package import PackageDto
    from app.model.environment import EnvironmentDto
    from app.model.config_file import ConfigFileDto


class Bucket(CustomBaseModel, table=True):
    user_token: str = ModelField(nullable=False)

    name: str = ModelField(default="", nullable=False)
    path: str = ModelField(default="", nullable=False)
    description: str = ModelField(default="", nullable=False)
    memo: str = ModelField(default="", nullable=False)
    is_published: bool = ModelField(default=True, nullable=False)

    # Platform and version info
    platform: str = ModelField(default="all", nullable=False)  # linux, macos, windows, all
    version: str = ModelField(default="1.0.0", nullable=False)

    # Installation guide
    readme: str = ModelField(default="", nullable=False)  # markdown format installation guide


class BucketDto:
    class Base(CustomBaseModelDto):
        name: str = Field(default="", nullable=False, example="local dev for python")
        path: str = Field(default="", nullable=False, example="local-dev-for-python")
        description: str = Field(default="", nullable=False, example="local dev for python")
        memo: str = Field(default="", nullable=False, example="local dev for python")
        is_published: bool = Field(default=True, nullable=False, example=True)
        platform: str = Field(default="all", nullable=False, example="all")
        version: str = Field(default="1.0.0", nullable=False, example="1.0.0")
        readme: str = Field(default="", nullable=False, example="# Installation Guide\n...")

    class WithBaseInfo(ModelBaseInfoDto, Base, metaclass=AllOptional):
        user_token: str = Field(..., description="user token", example="test_user_token")

    class WithAdditionalInfo(WithBaseInfo, metaclass=AllOptional):
        like_num: int = Field(default=0, example=0)
        is_liked: bool = Field(default=False, example=False)
        user_info: UserDto.Base = Field(default=None, example=None)
        is_published: bool = Field(default=True, nullable=False, example=True)

        # Additional environment information
        packages: list["PackageDto.WithAdditionalInfo"] | None = Field(None, description="packages", example=[])
        environments: list["EnvironmentDto.WithAdditionalInfo"] | None = Field(
            None, description="environments", example=[]
        )
        config_files: list["ConfigFileDto.WithAdditionalInfo"] | None = Field(
            None, description="config files", example=[]
        )

    class Upsert(Base, metaclass=AllOptional): ...

    class UpsertWithUserToken(Base, metaclass=AllOptional):
        user_token: str
