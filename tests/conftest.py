import asyncio
import os
import pytest
import pytest_asyncio
from loguru import logger

# overwrite ENV_NAME and prevent to run pytest from other environments
os.environ["ENV_NAME"] = "test"
if os.getenv("ENV_NAME") not in ["test"]:
    msg = f"ENV_NAME is not test, it is {os.getenv('ENV_NAME')}"
    pytest.exit(msg)
    
    
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def simple_fixture():
    logger.info("simple_fixture called")
    logger.info(f"simple_fixture id: {(id(simple_fixture))}")
    yield "simple_fixture"
