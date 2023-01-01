from dependency_injector.wiring import Container, Provide, inject
from fastapi import APIRouter, Depends

from app.model.user import AuthDto

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/sign-in", response_model=AuthDto.JWTPayload)
@inject
async def sign_in(user_info: AuthDto.SignIn, service: AuthService = Depends(Provide[Container.auth_service])):
    return service.sign_in(user_info)


@router.post("/sign-up", response_model=AuthDto.JWTPayload)
@inject
async def sign_up(user_info: AuthDto.SignUp, service: AuthService = Depends(Provide[Container.auth_service])):
    return service.sign_up(user_info)
