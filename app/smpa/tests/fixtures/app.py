import pytest
from smpa.app import create_app


@pytest.fixture
def app():
    application = create_app()
    application.req_options.auto_parse_form_urlencoded = True
    return application
