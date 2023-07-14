from asyncio import get_event_loop

import pytest_asyncio
from httpx import AsyncClient

from app.main import app


@pytest_asyncio.fixture(scope="module")
async def async_client():
    """
        Return AsyncClient for API requests
    """
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client


@pytest_asyncio.fixture(scope="session")
def event_loop():
    """
        Create event loop for launch FastAPI's server  for tests
    """
    loop = get_event_loop()
    yield loop
    loop.close()