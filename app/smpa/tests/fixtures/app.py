import pytest
from falcon import testing
from smpa.app import create_app

from pytest_falcon.plugin import Client


@pytest.fixture
def app():
    application = create_app()
    application.req_options.auto_parse_form_urlencoded = True
    return application


@pytest.fixture
def mock_client(app):
    return testing.TestClient(app)


@pytest.fixture(scope="session")
def session_app():
    application = create_app()
    application.req_options.auto_parse_form_urlencoded = True
    return application


@pytest.fixture(scope="session")
def session_client(session_app):
    """A session scoped client fixture for doing multiple tests
    without restarting the application between each one.

    Args:
        session_app (fixture): The session scoped app fixture

    Yields:
        test client
    """
    yield Client(session_app)
