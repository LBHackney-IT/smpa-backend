import falcon
from smpa.services.user import _users


def get_token(user=None):
    if not user:
        user = _users.first(email='test@example.com')
    token = _users.gen_token(user)
    return token


def test_test_user_exists():
    assert _users.first(email='test@example.com') is not None


def test_user_verify():
    user = _users.first(email='test@example.com')
    assert _users.verify(user, 'secretpassword') is True


def test_user_verify_fails_with_bad_password():
    user = _users.first(email='test@example.com')
    assert _users.verify(user, 'secretpassword1') is not True


def test_authenticate():
    user = _users.first(email='test@example.com')
    authed = _users.authenticate(
        {
            'email': 'test@example.com',
            'password': 'secretpassword'
        }
    )
    assert authed.id == user.id


def test_gen_token():
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
