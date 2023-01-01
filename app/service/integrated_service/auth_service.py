from datetime import timedelta

from app.core.config import configs
from app.core.exception import AuthError
from app.core.security import create_access_token, get_password_hash, verify_password
from app.model.user import AuthDto, User
from app.repository.user_repository import UserRepository
from app.service.base_service import BaseService
from app.utils.common import random_hash


class AuthService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        super().__init__(user_repository)

    def sign_in(self, sign_in_dto: AuthDto.SignIn):
        find_user.email__eq = sign_in_dto.email
        user: list[User] = self.user_repository.read_by_options(find_user)["founds"]
        if len(user) < 1:
            raise AuthError(detail="Incorrect email or password")
        found_user = user[0]
        if not found_user.is_activated:
            raise AuthError(detail="Account is not active")
        if not verify_password(sign_in_dto.password, found_user.password):
            raise AuthError(detail="Incorrect email or password")
        delattr(found_user, "password")
        payload = AuthDto.JWTPayload(
            email=found_user.email,
            nickname=found_user.nickname,
        )
        token_lifespan = timedelta(minutes=configs.JWT_ACCESS_EXPIRE)
        access_token, expiration_datetime = create_access_token(payload.dict(), token_lifespan)
        sign_in_result = {
            "access_token": access_token,
            "expiration": expiration_datetime,
            "user_info": found_user,
        }
        return sign_in_result

    async def sign_up(self, sing_up_dto: AuthDto.SignUp) -> AuthDto.JWTPayload:
        user_token = random_hash(length=12)
        user = User(**sing_up_dto.dict(exclude_none=True), is_activated=True, is_superuser=False, user_token=user_token)
        user.password = get_password_hash(sing_up_dto.password)
        created_user = await self.user_repository.insert(user)
        return AuthDto.JWTPayload(**created_user.dict())
