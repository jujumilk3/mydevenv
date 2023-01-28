from fastapi import APIRouter

from app.api.v1.endpoint.admin import router as admin_router
from app.api.v1.endpoint.auth import router as auth_router
from app.api.v1.endpoint.bucket import router as bucket_router

routers = APIRouter()
router_list = [
    admin_router,
    auth_router,
    bucket_router
    # user_router
]

for router in router_list:
    # router.tags = routers.tags.append("v1")  # If you want to add tags to each router, uncomment this line.
    routers.include_router(router)
