"""
    Test user related endpoints.
"""

import simplejson as json
import falcon
from .test_auth import get_token
from ..util import json_match, reset_test_user

from smpa.helpers.console import console


TOKEN = None
USER_ID = "b7d623db-5b4a-43df-b3f1-2bfca845d657"
USER2_ID = None
PROFILE_ID = None


reset_test_user()


def test_create_user(session_client):
    global USER2_ID
    rv = session_client.post(
        f'/api/v1/users/create',
        {
            'email': 'test3@example.com',
            'password': 'password123'
        }
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['message'] == "User created"


def test_update_email(session_client):
    global TOKEN
    global USER_ID
    TOKEN = get_token()
    body = json.dumps(
        {
            "email": "test2@example.com"
        }
    )
    rv = session_client.patch(
        f'/api/v1/users/{USER_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['email'] == "test2@example.com"
