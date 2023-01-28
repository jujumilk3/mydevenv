from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.dependency import get_current_super_user
from app.model.user import User
from app.service.integrated_service.tool_integrated_service import ToolIntegratedService

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)


@router.get("/check")
@inject
async def check_admin(
    user: User = Depends(get_current_super_user),
):
    return {"is_admin": user.is_superuser}


@router.post("/register/tool")
@inject
async def register_tool(
    user: User = Depends(get_current_super_user),
    tool_integrated_service: ToolIntegratedService = Depends(Provide[Container.tool_integrated_service]),
):
    return {"is_admin": user.is_superuser}
