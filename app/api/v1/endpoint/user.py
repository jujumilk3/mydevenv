from dependency_injector.wiring import Container, Provide, inject
from fastapi import APIRouter, Depends

from app.model.user import AuthDto

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

