from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.core.container import Container
from app.core.dependency import get_current_user_token, get_current_user_token_no_exception
from app.model.tag import TagDto
from app.service.tag_service import TagService

router = APIRouter(
    prefix="/tag",
    tags=["tag"],
)


@router.get("/{tag_id}")
@inject
async def get_tag(
    tag_id: int,
    tag_service: TagService = Depends(Provide[Container.tag_service]),
    user_token: str = Depends(get_current_user_token_no_exception),
):
    return await tag_service.get_by_id(model_id=tag_id)


@router.post("", response_model=TagDto.WithBaseInfo, status_code=status.HTTP_201_CREATED)
@inject
async def create_tag(
    tag_info: TagDto.Upsert,
    tag_service: TagService = Depends(Provide[Container.tag_service]),
    user_token: str = Depends(get_current_user_token),
):
    return await tag_service.add(TagDto.UpsertWithUserToken(**tag_info.dict(), user_token=user_token))


@router.patch("/{tag_id}", response_model=TagDto.WithBaseInfo, status_code=status.HTTP_200_OK)
@inject
async def update_tag(
    tag_id: int,
    tag_info: TagDto.Upsert,
    tag_service: TagService = Depends(Provide[Container.tag_service]),
    user_token: str = Depends(get_current_user_token),
):
    return await tag_service.patch_by_id_after_check_user_token(
        model_id=tag_id,
        dto=TagDto.UpsertWithUserToken(**tag_info.dict(), user_token=user_token),
        user_token=user_token,
    )


@router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_tag(
    tag_id: int,
    tag_service: TagService = Depends(Provide[Container.tag_service]),
    user_token: str = Depends(get_current_user_token),
):
    await tag_service.remove_by_id_after_check_user_token(model_id=tag_id, user_token=user_token)
