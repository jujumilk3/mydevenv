import pytest

@pytest.mark.asyncio
async def test_one_plus_one():
    assert 1 + 1 == 2

@pytest.mark.asyncio    
async def test_simple_fixture(simple_fixture):
    assert simple_fixture == "simple_fixture"
