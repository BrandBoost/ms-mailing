import typing as tp
from asyncio import get_event_loop
from datetime import datetime, timedelta

import jwt
import pytest_asyncio
from httpx import AsyncClient

from app.config import settings
from app.main import app

TOKEN_CREATE_HELPING_DATA: tp.Any = {
    'refresh': {
        'expire': settings.JWT_REFRESH_TTL,
        'subject': settings.REFRESH_TOKEN_JWT_SUBJECT
    },
    'access': {
        'expire': settings.JWT_ACCESS_TTL,
        'subject': settings.ACCESS_TOKEN_JWT_SUBJECT
    }
}


@pytest_asyncio.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client


@pytest_asyncio.fixture
async def access_token_with_id():
    token_id = "1"
    access_token = await create_token("access", token_id)
    headers = {
        "Authorization": f"{settings.TOKEN_TYPE} {access_token}"
    }
    return headers


async def create_token(token_type: str, user_id: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=float(TOKEN_CREATE_HELPING_DATA[token_type]['expire']))

    payload = {
        'id': user_id,
        'exp': expire,
        'sub': TOKEN_CREATE_HELPING_DATA[token_type]['subject'],
    }
    encoded_jwt: str = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


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
