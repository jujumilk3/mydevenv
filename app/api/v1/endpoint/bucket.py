from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette import status

from app.core.container import Container
from app.core.dependency import get_current_active_user
from app.model.bucket import BucketDto
from app.model.user import User
from app.service.integrated_service.auth_service import AuthService

router = APIRouter(
    prefix="/bucket",
    tags=["bucket"],
)


@router.post("", response_model=BucketDto.WithBaseInfo, status_code=status.HTTP_201_CREATED)
@inject
async def create_bucket(
    bucket_info: BucketDto.Upsert,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
    current_user: User = Depends(get_current_active_user),
):
    return await auth_service.create_bucket(bucket_info, current_user)
