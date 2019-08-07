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
USER_PROFILE_ID = None


user = reset_test_user()


def test_get_user(session_client):
    global TOKEN
    global USER_PROFILE_ID
    TOKEN = get_token()
    rv = session_client.get(
        f'/api/v1/users/{USER_ID}',
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['profile_id'] is not None
    assert j['profile'] is not None
    USER_PROFILE_ID = j['profile_id']


def test_profile_update(session_client):
    body = json.dumps(
        {
            "company": {
                "company_name": "Acme Architecture",
                "address_line_1": "1 Some Street",
                "address_line_2": "Hackney",
                "city": "London",
                "postcode": "E8 1BB",
                "phone": "02071234567",
                "email": {
                    "email_address": "test4@example.com"
                }
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/user-profiles/{USER_PROFILE_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['company']['company_name'] == "Acme Architecture"


def test_update_email(session_client):
    global TOKEN
    global USER_ID
    global USER_PROFILE_ID
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
    assert j['profile']['id'] is not None
    USER_PROFILE_ID = j['profile']['id']
