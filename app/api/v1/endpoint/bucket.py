from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.core.container import Container
from app.core.dependency import get_current_user_token, get_current_user_token_no_exception
from app.model.bucket import BucketDto
from app.service.bucket_service import BucketService

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
