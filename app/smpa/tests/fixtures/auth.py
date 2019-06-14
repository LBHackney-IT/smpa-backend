import pytest
from ..test_endpoints.test_auth import get_token


@pytest.fixture
def token():
    return get_token()
