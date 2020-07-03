"""
    Test various account related functions.
"""

from smpa.services.user import _users, _roles


VERIFICATION_TOKEN = '1014f225-e580-447d-8908-39ebf860fbc5'


def _unverified_user():
    user_role = _roles.get_or_create(name='User')
    u = _users.get_or_create(
        id='aa5a9d16-e230-48bd-a381-0a314973a27f',
        email='temp@example.com',
        password='somepassword',
        verification_token=VERIFICATION_TOKEN,
        role_id=str(user_role.id)
    )
    _users.save(u)
    return u


def test_verify_account_service_method():
    u = _unverified_user()
    assert u.verified_at is None
    verified = _users.verify_account(VERIFICATION_TOKEN)
    assert verified is not None
    assert verified.verified_at is not None
    assert u.email == verified.email


def test_user_roles(user_user, user_admin, user_superadmin):
    assert _users.count() == 4
    assert user_user.role.name == 'User'
    assert user_admin.role.name == 'Admin'
    assert user_superadmin.role.name == 'SuperAdmin'
