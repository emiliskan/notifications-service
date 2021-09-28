from dataclasses import dataclass

import aiohttp
import pytest
from multidict import CIMultiDictProxy

from .settings import SERVICE_URL, API_URL


@dataclass
class HTTPResponse:
    body: dict
    headers: CIMultiDictProxy[str]
    status: int


@pytest.fixture
async def session():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest.fixture
def make_post_request(session):
    async def inner(method: str, params: dict = None) -> HTTPResponse:
        url = f"http://{SERVICE_URL}{API_URL}{method}"
        async with session.post(url, params=params) as response:
            return HTTPResponse(
                body=await response.json(),
                headers=response.headers,
                status=response.status,
            )
    return inner


@pytest.fixture
def make_post_request(session):
    async def inner(url: str, data: dict = None,
                    headers: dict = None) -> HTTPResponse:
        url = f"http://{SERVICE_URL}{API_URL}{url}"
        async with session.post(url, json=data, headers=headers) as response:
            return HTTPResponse(
                body=await response.json(),
                headers=response.headers,
                status=response.status,
            )
    return inner
