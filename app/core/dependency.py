from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from jose import jwt
from pydantic import ValidationError

from app.core.config import configs
from app.core.container import Container
from app.core.exception import AuthError
from app.core.security import JWTBearer
from app.model.user import AuthDto, User
from app.service.user_service import UserService


@inject
async def get_current_user(
    token: str = Depends(JWTBearer()),
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> User:
    try:
        payload = jwt.decode(token, configs.JWT_SECRET_KEY, algorithms=configs.JWT_ALGORITHM)
        token_data = AuthDto.Payload(**payload)
    except (jwt.JWTError, ValidationError) as e:
        raise AuthError(detail="Could not validate credentials") from e
    current_user: User = await user_service.get_user_by_user_token(token_data.user_token)
    if not current_user:
        raise AuthError(detail="User not found")
    current_user.password = "***"
    return current_user


def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_activated:
        raise AuthError("Inactive user")
    return current_user


async def get_current_user_with_no_exception(
    token: str = Depends(JWTBearer()),
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> User | None:
    try:
        payload = jwt.decode(token, configs.JWT_SECRET_KEY, algorithms=configs.JWT_ALGORITHM)
        token_data = AuthDto.Payload(**payload)
    except (jwt.JWTError, ValidationError):
        return None
    current_user: User = await user_service.get_user_by_user_token(token_data.user_token)
    if not current_user:
        return None
    return current_user


def get_current_super_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_activated:
        raise AuthError("Inactive user")
    if not current_user.is_superuser:
        raise AuthError("It's not a super user")
    return current_user
