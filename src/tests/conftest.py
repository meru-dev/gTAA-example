import pytest

from src.adapters.api.http.rest_http_client import RestHttpClient
from src.generic.clients.api.http.auth.client import AuthApi
from src.generic.setup.config import config
from src.generic.steps.auth_steps import AuthSteps


@pytest.fixture(scope="session")
def test_config():
    return config


@pytest.fixture(scope="session")
def rest_http_client(test_config):
    return RestHttpClient(test_config.base_url)


@pytest.fixture(scope="session")
def auth_api(rest_http_client):
    return AuthApi(rest_http_client)


@pytest.fixture(scope="session")
def auth_steps(auth_api):
    return AuthSteps(auth_api)
