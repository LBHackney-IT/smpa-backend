import os
import simplejson as json
import falcon
import pytest  # NOQA

from .test_auth import get_token

APPLICATION_ID = "9e7cf43a-6860-4061-b585-65b4fb778a30"
TOKEN = None

ID_STR = "cbddcfc8-d062-4202-b350-f875c04c6aa0,f1ff39d9-aab3-46e3-8749-dad11c04e3b8"


def test_posted_image_gets_saved(client, monkeypatch):
    global TOKEN
    TOKEN = get_token()
    here = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join('..', here, 'images', 'test-image.png')
    image = open(filepath, 'rb')
    rv = client.post(
        f'/api/v1/documents',
        data={
            "application_id": APPLICATION_ID,
            "document_size_id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
            "existing_str": ID_STR,
            "proposed_str": ID_STR
        },
        files={
            "document": image
        },
        headers={
            'content-type': 'image/png',
            "Authorization": f"jwt {TOKEN}"
        }
    )

    assert rv.status == falcon.HTTP_CREATED
    j = json.loads(rv.body)
    assert j['id'] is not None
    assert j['original_name'] == 'test-image.png'
    assert '.png' in j['storage_path']
    assert j['document_size']['name'] == 'A1'


def test_empty_existing_str(client, monkeypatch):
    global TOKEN
    TOKEN = get_token()
    here = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join('..', here, 'images', 'test-image.png')
    image = open(filepath, 'rb')
    rv = client.post(
        f'/api/v1/documents',
        data={
            "application_id": APPLICATION_ID,
            "document_size_id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
            "existing_str": "",
            "proposed_str": ID_STR
        },
        files={
            "document": image
        },
        headers={
            'content-type': 'image/png',
            "Authorization": f"jwt {TOKEN}"
        }
    )

    assert rv.status == falcon.HTTP_CREATED
    j = json.loads(rv.body)
    assert j['id'] is not None
    assert j['original_name'] == 'test-image.png'
    assert '.png' in j['storage_path']
    assert j['document_size']['name'] == 'A1'
    assert j['document_types_existing'] == []
    assert j['document_types_existing_ids'] == []
