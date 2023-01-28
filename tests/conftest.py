import asyncio
import os

import pytest
import pytest_asyncio
from loguru import logger

# overwrite ENV and prevent to run pytest from other environments
os.environ["ENV"] = "test"
if os.getenv("ENV") not in ["test"]:
    msg = f"ENV is not test, it is {os.getenv('ENV')}"
    pytest.exit(msg)

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from starlette.testclient import TestClient

from app.main import app
from tests.utils.common import read_test_data_from_test_file
from tests.utils.router_for_test import router as basic_router_for_test


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


async def create_tables(engine):
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
        await insert_default_test_data(conn)


@pytest.fixture(scope="session")
def client():
    logger.info("pytest just started")
    logger.info(f"ENV: {os.getenv('ENV')}")
    app.include_router(basic_router_for_test, prefix="/test_only")
    logger.info("client fixture started")
    asyncio.run(create_tables(app.db.engine))
    yield TestClient(app)


async def insert_default_test_data(conn):
    super_users = read_test_data_from_test_file("user/super_users.json")
    print(super_users)
    logger.info("Just started insert_default_test_data")


@pytest.fixture(scope="session")
async def engine():
    logger.info("engine fixture started")
    logger.info(f"engine id: {id(engine)}")
    _engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with _engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
        await insert_default_test_data(conn)
        yield conn


@pytest.fixture
def test_name(request):
    return request.node.name
