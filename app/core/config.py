import os
from pathlib import Path

from loguru import logger


class BaseConfigs:
    # base
    ENV: str = "dev"
    APP_ROOT_DIR: str = Path(__file__).parent.parent.parent
    TEST_DATA_DIR: str = os.path.join(APP_ROOT_DIR, "tests", "data")
    PROJECT_NAME: str = "mydevenv"

    # api addresses
    API_PREFIX: str = ""  # /api
    API_V1_STR: str = "/v1"
    API_V2_STR: str = "/v2"

    # auth
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "mydevenv")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_EXPIRE: int = 60 * 60 * 24 * 7  # 7 days
    JWT_REFRESH_EXPIRE: int = 60 * 60 * 24 * 30  # 30 days

    # date
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    # cors
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    # database
    DB_URL = "sqlite+aiosqlite:///db.sqlite3"
    SYNC_DB_URL = "sqlite:///db.sqlite3"


class TestConfigs(BaseConfigs):
    # base
    ENV: str = "test"
    DB_URL = "sqlite+aiosqlite:///:memory:"


class DevelopConfigs(BaseConfigs):
    # base
    ENV: str = "dev"


class StageConfigs(BaseConfigs):
    # base
    ENV: str = "stage"


class ProductionConfigs(BaseConfigs):
    # base
    ENV: str = "prod"


ENV: str = os.getenv("ENV", "")

configs = BaseConfigs()

if ENV == "prod":
    configs = ProductionConfigs()
elif ENV == "stage":
    configs = StageConfigs()
elif ENV == "dev":
    configs = DevelopConfigs()
elif ENV == "test":
    configs = TestConfigs()
else:
    logger.info("ENV is not set. Use BaseConfigs.")
    configs = BaseConfigs()
