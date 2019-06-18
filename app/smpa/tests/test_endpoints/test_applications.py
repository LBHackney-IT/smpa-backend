import falcon
from .test_auth import get_token


def test_get_unauthorized(client):
    rv = client.get('/api/v1/applications')
    assert rv.status != falcon.HTTP_OK


# def test_post(client):
#     token = get_token()
#     rv = client.post(
#         '/api/v1/applications',
#         {},
#         headers={"Authorization": f"jwt {token}"}
#     )
#     assert rv.status == falcon.HTTP_OK


def test_get_authorized(client):
    token = get_token()
    rv = client.get(
        '/api/v1/applications',
        headers={"Authorization": f"jwt {token}"}
    )
    assert rv.status == falcon.HTTP_OK


def test_get_application_404(client, token):
    """Sends a bad uuid in the hope of a 404
    """
    rv = client.get(
        '/api/v1/applications/ee2bda96-0585-4668-b041-5755ce4c40fe',
        headers={"Authorization": f"jwt {token}"}
    )
    assert rv.status == falcon.HTTP_404


def test_applications_404(client, token):
    """Sends a good uuid
    """
    rv = client.get(
        '/api/v1/applications/9e7cf43a-6860-4061-b585-65b4fb778a30',
        headers={"Authorization": f"jwt {token}"}
    )
    assert rv.status == falcon.HTTP_OK
    assert rv.json['works_description'] == 'I did a thing to my house'
