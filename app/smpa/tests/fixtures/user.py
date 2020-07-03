import arrow
import pytest

from smpa.services.user import _roles, _users


@pytest.fixture
def role_user():
    role = _roles.get_or_create(name='User')
    return role


@pytest.fixture
def role_admin():
    role = _roles.get_or_create(name='Admin')
    return role


@pytest.fixture
def role_superadmin():
    role = _roles.get_or_create(name='SuperAdmin')
    return role


@pytest.fixture
def user_user(role_user):
    role = _roles.first(name='User')
    role_id = str(role.id)
    u = _users.get_or_create(
        email='user@example.com',
        password='123',
        role_id=role_id
    )
    u.verified_at = arrow.utcnow().datetime
    u = _users.save(u)
    return u


@pytest.fixture
def user_admin(role_admin):
    role = _roles.first(name='Admin')
    role_id = str(role.id)
    u = _users.get_or_create(
        email='admin@example.com',
        password='123',
        role_id=role_id
    )
    u.verified_at = arrow.utcnow().datetime
    u = _users.save(u)
    return u


@pytest.fixture
def user_superadmin(role_superadmin):
    role = _roles.first(name='SuperAdmin')
    role_id = str(role.id)
    u = _users.get_or_create(
        email='superadmin@example.com',
        password='123',
        role_id=role_id
    )
    u.verified_at = arrow.utcnow().datetime
    u = _users.save(u)
    return u
