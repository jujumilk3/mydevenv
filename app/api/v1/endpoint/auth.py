from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.model.user import AuthDto
from app.service.integrated_service.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/sign-in", response_model=AuthDto.JWTPayload)
@inject
async def sign_in(user_info: AuthDto.SignIn, service: AuthService = Depends(Provide[Container.auth_service])):
    return service.sign_in(user_info)


@router.post("/sign-up", response_model=AuthDto.JWTPayload)
@inject
async def sign_up(user_info: AuthDto.SignUp, service: AuthService = Depends(Provide[Container.auth_service])):
    return await service.sign_up(user_info)
