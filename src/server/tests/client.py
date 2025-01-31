import pytest
from httpx import AsyncClient
from server.asgi import application

TEST_IMAGE_NAME: str = "nginx"
TEST_PULL_IMAGE: str = "hello-world"
TEST_IMAGE_FULLNAME: str = "nginx:1.18-alpine"


@pytest.fixture
def client():
    global application

    return AsyncClient(
        app=application,
        timeout=60*2,  # seconds
        base_url="http://127.0.0.1:2121/api/"
    )


__all__ = [
    "client",
    "application",
    "TEST_IMAGE_NAME",
    "TEST_PULL_IMAGE",
    "TEST_IMAGE_FULLNAME"
]
