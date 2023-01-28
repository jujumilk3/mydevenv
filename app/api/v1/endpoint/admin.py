from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.core.container import Container
from app.core.dependency import get_current_super_user
from app.model.tool import ToolDto
from app.model.user import User
from app.service.integrated_service.tool_integrated_service import ToolIntegratedService

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)


@router.get("/check", responses={200: {"content": {"application/json": {"example": {"is_admin": True}}}}})
@inject
async def check_admin(
    user: User = Depends(get_current_super_user),
):
    return {"is_admin": user.is_superuser}


@router.post("/tool", response_model=ToolDto.WithAdditionalInfo, status_code=status.HTTP_201_CREATED)
@inject
async def register_tool(
    tool_upsert: ToolDto.Upsert,
    *,
    user: User = Depends(get_current_super_user),
    tool_integrated_service: ToolIntegratedService = Depends(Provide[Container.tool_integrated_service]),
):
    return await tool_integrated_service.create_tool(tool_upsert=tool_upsert)


@router.patch("/tool/{tool_id}", response_model=ToolDto.WithAdditionalInfo, status_code=status.HTTP_200_OK)
@inject
async def update_tool(
    tool_id: int,
    tool_upsert: ToolDto.Upsert,
    *,
    user: User = Depends(get_current_super_user),
    tool_integrated_service: ToolIntegratedService = Depends(Provide[Container.tool_integrated_service]),
):
    return await tool_integrated_service.patch_tool_by_id(tool_id=tool_id, tool_upsert=tool_upsert)


@router.delete("/tool/{tool_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_tool(
    tool_id: int,
    *,
    user: User = Depends(get_current_super_user),
    tool_integrated_service: ToolIntegratedService = Depends(Provide[Container.tool_integrated_service]),
):
    return await tool_integrated_service.remove_tool_by_id(tool_id=tool_id)
