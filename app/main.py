from fastapi import FastAPI
from loguru import logger
from starlette import status
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.route import routers as v1_router
from app.core.config import configs
from app.core.container import Container


def create_app():
    _app = FastAPI(
        title=configs.PROJECT_NAME,
        docs_url=f"{configs.API_PREFIX}/docs",
        redoc_url=f"{configs.API_PREFIX}/redoc",
        openapi_url=f"{configs.API_PREFIX}/openapi.json",
        version="0.0.1",
    )

    # set db and container
    container = Container()
    _app.container = container
    _app.db = container.db()

    # set cors
    if configs.BACKEND_CORS_ORIGINS:
        _app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in configs.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # set routes
    @_app.get(f"{configs.API_PREFIX}/healthcheck", status_code=status.HTTP_200_OK)
    def root():
        return "OK"

    _app.include_router(v1_router, prefix=configs.API_V1_STR)
    logger.info(f"app created. Its ENV_NAME: {configs.ENV}")
    return _app


app = create_app()
