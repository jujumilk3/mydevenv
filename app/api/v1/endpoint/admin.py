from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.dependency import get_current_active_user_token
from app.model.user import User
from app.service.user_service import UserService

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)


@router.get("/check")
@inject
async def check_admin(
    user_token: str = Depends(get_current_active_user_token),
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    user: User = await user_service.get_user_by_user_token(user_token)
    return {"is_admin": user.is_superuser}
