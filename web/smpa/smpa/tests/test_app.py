import pytest

from ..app import app
from molten import testing


@pytest.fixture(scope="session")
def client():
    return testing.TestClient(app)


def test_app_factory(client):
    assert hasattr(app, 'reverse_uri')


def test_can_create_address(client):
    response = client.post(
        '/addresses/create',
        # app.reverse_uri("create_address"),
        json={"description": "example"},
    )
    assert response.status_code == 200
    assert response.json()["description"] == "example"
