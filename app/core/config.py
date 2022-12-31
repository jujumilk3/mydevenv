import os
from pathlib import Path


class BaseConfigs:
    # base
    ENV: str = os.getenv("ENV", "")
    APP_ROOT_DIR: str = Path(__file__).parent.parent.parent
    PROJECT_NAME: str = "mydevenv"

    # internal addressed
    API_V1_STR: str = f"/v1"
    API_V2_STR: str = f"/v2"

    # cors
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    # database
    DB_URL = "sqlite+aiosqlite:///:memory:"


class TestConfigs(BaseConfigs):
    # base    
    ENV: str = "test"


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
    print("ENV is not set.")
    configs = BaseConfigs()
