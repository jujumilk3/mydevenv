from fastapi import APIRouter

from app.api.v1.endpoint.admin import router as admin_router
from app.api.v1.endpoint.auth import router as auth_router
from app.api.v1.endpoint.bucket import router as bucket_router
from app.api.v1.endpoint.tag import router as tag_router
from app.api.v1.endpoint.tool import router as tool_router
from app.api.v1.endpoint.user import router as user_router

routers = APIRouter()
router_list = [admin_router, auth_router, bucket_router, tag_router, tool_router, user_router]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)
