import pytest

from ..app import app
from molten import testing


@pytest.fixture(scope="session")
def client():
    return testing.TestClient(app)


def test_can_create_todos(client):
    response = client.post(
        app.reverse_uri("create_todo"),
        json={"description": "example"},
    )
    assert response.status_code == 200
    assert response.json()["description"] == "example"
