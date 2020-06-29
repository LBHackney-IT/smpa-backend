import falcon
import responses

from smpa.services.user import _users

from ..util import json_match, reset_test_user


# https://api.notifications.service.gov.uk/v2/notifications/email


SEND_VERIFICATION_EMAIL_RESPONSE = {
    'content': {
        'body': 'email body goes here',
        'from_email': 'submit.my.planning.application@notifications.service.gov.uk',
        'subject': 'Confirm your Submit my Planning Application account'
    },
    'id': '91626a62-4557-46d8-90a1-7303b75f9f78',
    'reference': None,
    'scheduled_for': None,
    'template': {
        'id': 'd4c144d2-3cb6-400e-bdb6-6b0dd5dbd087',
        'uri': 'template url goes here',
        'version': 1
    },
    'uri': 'some other url goes here'
}


def get_token(user=None, email=None):
    if user is None and email is not None:
        user = _users.first(email=email)
    elif user is None and email is None:
        reset_test_user()
        user = _users.first(email='test@example.com')
    token = _users.gen_token(user)
    return token


def test_test_user_exists(session_client):
    assert _users.first(email='test@example.com') is not None


def test_user_verify(session_client):
    reset_test_user()
    user = _users.first(email='test@example.com')
    assert _users.verify(user, 'secretpassword') is True


def test_user_verify_fails_with_bad_password(session_client):
    user = _users.first(email='test@example.com')
    assert _users.verify(user, 'secretpassword1') is not True


def test_authenticate(session_client):
    user = _users.first(email='test@example.com')
    authed = _users.authenticate(
        {
            'email': 'test@example.com',
            'password': 'secretpassword'
        }
    )
    assert authed.id == user.id


def test_gen_token(session_client):
    token = get_token()
    assert isinstance(token, str)
    assert len(token) > 150


def test_log_in(app, client):
    rv = client.post(
        '/api/v1/auth',
        {
            'email': 'test@example.com',
            'password': 'secretpassword'
        }
    )
    assert rv.status == falcon.HTTP_OK


@responses.activate
def test_register_service(session_client):
    responses.add(
        responses.POST,
        'https://api.notifications.service.gov.uk/v2/notifications/email',
        json=SEND_VERIFICATION_EMAIL_RESPONSE,
        status=200
    )
    rv = _users.register('test99@example.com', 'secretpassword')
    assert rv is not None
    assert rv.email == 'test99@example.com'
    assert rv.verified_at is None
    assert rv.verified is False
    assert rv.verification_token is not None
    assert 'SuperUser' not in rv


def test_log_in_fails_for_unverified_account(app, session_client):
    rv = session_client.post(
        '/api/v1/auth',
        {
            'email': 'test99@example.com',
            'password': 'secretpassword'
        }
    )
    assert rv.status == falcon.HTTP_401
    assert rv.json['title'] == 'Account is not yet verified'


@responses.activate
def test_verify_account_service(session_client):
    responses.add(
        responses.POST,
        'https://api.notifications.service.gov.uk/v2/notifications/email',
        json=SEND_VERIFICATION_EMAIL_RESPONSE,
        status=200
    )
    user = _users.first(email='test99@example.com')
    assert user is not None
    assert user.verified_at is None
    assert user.verification_token is not None
    rv = _users.verify_account(user.verification_token)
    assert rv is not None
    assert rv.verified is True
    assert rv.verified_at is not None


def test_log_in_now_verified(app, session_client):
    rv = session_client.post(
        '/api/v1/auth',
        {
            'email': 'test99@example.com',
            'password': 'secretpassword'
        }
    )
    assert rv.status == falcon.HTTP_OK


@responses.activate
def test_register_endpoint(session_client):
    responses.add(
        responses.POST,
        'https://api.notifications.service.gov.uk/v2/notifications/email',
        json=SEND_VERIFICATION_EMAIL_RESPONSE,
        status=200
    )
    rv = session_client.post(
        '/api/v1/users/create',
        {
            'email': 'test101@example.com',
            'password': 'secretpassword',
            'password_confirm': 'secretpassword'
        }
    )
    assert rv is not None
    j = rv.json
    assert j['email'] == 'test101@example.com'
    assert j['verified_at'] is None


def test_verify_endpoint(session_client):
    vtoken = _users.first(email='test101@example.com').verification_token
    rv = session_client.get(
        f'/api/v1/users/verify/{vtoken}'
    )
    assert rv is not None
    j = rv.json
    assert j['message'] == 'Account verified and logged in'
    assert j['jwt'] is not None


def test_verify_endpoint_already_verified(session_client):
    vtoken = _users.first(email='test101@example.com').verification_token
    rv = session_client.get(
        f'/api/v1/users/verify/{vtoken}'
    )
    assert rv is not None
    assert rv.status == falcon.HTTP_400
    j = rv.json
    assert j['title'] == 'Account already verified'


def test_verify_endpoint_bad_token(session_client):
    rv = session_client.get(
        f'/api/v1/users/verify/aljdlafjlkjflkfjd'
    )
    assert rv is not None
    assert rv.status == falcon.HTTP_400
    j = rv.json
    assert j['title'] == 'Invalid verification token'


def test_log_in_now_verified_again(app, session_client):
    rv = session_client.post(
        '/api/v1/auth',
        {
            'email': 'test101@example.com',
            'password': 'secretpassword'
        }
    )
    assert rv.status == falcon.HTTP_OK
