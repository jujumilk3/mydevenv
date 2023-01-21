from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette import status

from app.core.container import Container
from app.core.dependency import get_current_active_user
from app.model.bucket import BucketDto
from app.model.user import User
from app.service.bucket_service import BucketService

router = APIRouter(
    prefix="/bucket",
    tags=["bucket"],
)


@router.post("", response_model=BucketDto.WithBaseInfo, status_code=status.HTTP_201_CREATED)
@inject
async def create_bucket(
    bucket_info: BucketDto.Upsert,
    bucket_service: BucketService = Depends(Provide[Container.bucket_service]),
    current_user: User = Depends(get_current_active_user),
):
    return await bucket_service.add(BucketDto.UpsertWithUserToken(**bucket_info.dict(), user_token=current_user.user_token))
