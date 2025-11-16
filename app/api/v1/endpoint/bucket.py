from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import PlainTextResponse, Response

from app.core.container import Container
from app.core.dependency import get_current_user_token, get_current_user_token_no_exception
from app.model.bucket import BucketDto
from app.service.bucket_service import BucketService
from app.service.export_service import ExportService

router = APIRouter(
    prefix="/bucket",
    tags=["bucket"],
)


@router.get("/{bucket_id}")
@inject
async def get_bucket(
    bucket_id: int,
    *,
    bucket_service: BucketService = Depends(Provide[Container.bucket_service]),
    user_token: str = Depends(get_current_user_token_no_exception),
):
    return await bucket_service.get_by_id(model_id=bucket_id)


@router.post("", response_model=BucketDto.WithBaseInfo, status_code=status.HTTP_201_CREATED)
@inject
async def create_bucket(
    bucket_upsert: BucketDto.Upsert,
    *,
    bucket_service: BucketService = Depends(Provide[Container.bucket_service]),
    user_token: str = Depends(get_current_user_token),
):
    return await bucket_service.add(BucketDto.UpsertWithUserToken(**bucket_upsert.dict(), user_token=user_token))


@router.patch("/{bucket_id}", response_model=BucketDto.WithBaseInfo, status_code=status.HTTP_200_OK)
@inject
async def update_bucket(
    bucket_id: int,
    bucket_upsert: BucketDto.Upsert,
    *,
    bucket_service: BucketService = Depends(Provide[Container.bucket_service]),
    user_token: str = Depends(get_current_user_token),
):
    return await bucket_service.patch_by_id_after_check_user_token(
        model_id=bucket_id,
        dto=BucketDto.UpsertWithUserToken(**bucket_upsert.dict(), user_token=user_token),
        user_token=user_token,
    )


@router.delete("/{bucket_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_bucket(
    bucket_id: int,
    *,
    bucket_service: BucketService = Depends(Provide[Container.bucket_service]),
    user_token: str = Depends(get_current_user_token),
):
    await bucket_service.remove_by_id_after_check_user_token(model_id=bucket_id, user_token=user_token)


@router.get("/{bucket_id}/export", response_class=PlainTextResponse)
@inject
async def export_bucket(
    bucket_id: int,
    format: str = Query("json", description="Export format: json, yaml"),
    *,
    bucket_service: BucketService = Depends(Provide[Container.bucket_service]),
    user_token: str = Depends(get_current_user_token_no_exception),
):
    """Export bucket configuration to JSON or YAML"""
    bucket = await bucket_service.get_by_id(model_id=bucket_id)
    bucket_dict = bucket.dict() if hasattr(bucket, "dict") else dict(bucket)

    if format == "json":
        return Response(
            content=ExportService.export_to_json(bucket_dict),
            media_type="application/json",
            headers={"Content-Disposition": f"attachment; filename=bucket_{bucket_id}.json"},
        )
    elif format == "yaml":
        return Response(
            content=ExportService.export_to_yaml(bucket_dict),
            media_type="text/yaml",
            headers={"Content-Disposition": f"attachment; filename=bucket_{bucket_id}.yaml"},
        )
    else:
        return {"error": "Invalid format. Use 'json' or 'yaml'"}


@router.get("/{bucket_id}/install-script", response_class=PlainTextResponse)
@inject
async def get_install_script(
    bucket_id: int,
    script_type: str = Query("bash", description="Script type: bash, powershell, dockerfile, docker-compose"),
    *,
    bucket_service: BucketService = Depends(Provide[Container.bucket_service]),
    user_token: str = Depends(get_current_user_token_no_exception),
):
    """Generate installation script for the bucket"""
    bucket = await bucket_service.get_by_id(model_id=bucket_id)
    bucket_dict = bucket.dict() if hasattr(bucket, "dict") else dict(bucket)

    script_content = ExportService.generate_install_script(bucket_dict, script_type)

    file_extensions = {
        "bash": "sh",
        "powershell": "ps1",
        "dockerfile": "Dockerfile",
        "docker-compose": "docker-compose.yml",
    }

    filename = file_extensions.get(script_type, "sh")
    if script_type in ["dockerfile", "docker-compose"]:
        filename = file_extensions[script_type]
    else:
        filename = f"install.{filename}"

    return Response(
        content=script_content,
        media_type="text/plain",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@router.get("/{bucket_id}/export-all")
@inject
async def export_all(
    bucket_id: int,
    *,
    bucket_service: BucketService = Depends(Provide[Container.bucket_service]),
    user_token: str = Depends(get_current_user_token_no_exception),
):
    """Export complete package with all formats"""
    bucket = await bucket_service.get_by_id(model_id=bucket_id)
    bucket_dict = bucket.dict() if hasattr(bucket, "dict") else dict(bucket)

    return ExportService.export_complete_package(bucket_dict)
