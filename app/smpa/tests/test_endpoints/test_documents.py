import falcon
import pytest  # NOQA
from unittest.mock import mock_open, call

from .test_auth import get_token

APPLICATION_ID = "9e7cf43a-6860-4061-b585-65b4fb778a30"
TOKEN = None


def test_posted_image_gets_saved(client, monkeypatch):
    global TOKEN
    TOKEN = get_token()
    mock_file_open = mock_open()
    monkeypatch.setattr('io.open', mock_file_open)

    fake_uuid = '123e4567-e89b-12d3-a456-426655440000'
    monkeypatch.setattr('uuid.uuid4', lambda: fake_uuid)

    # When the service receives an image through POST...
    fake_image_bytes = b'fake-image-bytes'
    response = client.post(
        f'/api/v1/documents/upload/{APPLICATION_ID}',
        body=fake_image_bytes,
        headers={
            'content-type': 'image/png',
            "Authorization": f"jwt {TOKEN}"
        }
    )

    # ...it must return a 201 code, save the file, and return the
    # image's resource location.
    assert response.status == falcon.HTTP_CREATED
    assert call().write(fake_image_bytes) in mock_file_open.mock_calls
    assert response.headers['location'] == '/images/{}.png'.format(fake_uuid)


# def test_posted_image_gets_saved(mock_client, monkeypatch):
#     global TOKEN
#     TOKEN = get_token()
#     mock_file_open = mock_open()
#     monkeypatch.setattr('io.open', mock_file_open)

#     fake_uuid = '123e4567-e89b-12d3-a456-426655440000'
#     monkeypatch.setattr('uuid.uuid4', lambda: fake_uuid)

#     # When the service receives an image through POST...
#     fake_image_bytes = b'fake-image-bytes'
#     response = mock_client.simulate_post(
#         f'/api/v1/documents/upload/{APPLICATION_ID}',
#         body=fake_image_bytes,
#         headers={
#             'content-type': 'image/png',
#             "Authorization": f"jwt {TOKEN}"
#         }
#     )

#     # ...it must return a 201 code, save the file, and return the
#     # image's resource location.
#     assert response.status == falcon.HTTP_CREATED
#     assert call().write(fake_image_bytes) in mock_file_open.mock_calls
#     assert response.headers['location'] == '/images/{}.png'.format(fake_uuid)
