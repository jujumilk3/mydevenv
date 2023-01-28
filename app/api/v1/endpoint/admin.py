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


@router.post("/register/tool", response_model=ToolDto.WithAdditionalInfo, status_code=status.HTTP_201_CREATED)
@inject
async def register_tool(
    tool_upsert: ToolDto.Upsert,
    *,
    user: User = Depends(get_current_super_user),
    tool_integrated_service: ToolIntegratedService = Depends(Provide[Container.tool_integrated_service]),
):
    return await tool_integrated_service.register_tool(tool_upsert=tool_upsert)
