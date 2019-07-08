# -*- coding: utf-8 -*-

"""
    services.user
    ~~~~~~~~~~~~~
    User services.
"""

import arrow
import falcon
from typing import Optional
from passlib.hash import bcrypt
from ..models.user import Role, User, Agent, Applicant, UserProfile
from ..helpers.console import console  # NOQA

from .rethink import RService


class UserProfileService(RService):
    __model__ = UserProfile


_user_profiles = UserProfileService()


class UserService(RService):
    __model__ = User

    @staticmethod
    def verify(user, password):
        if user is None:
            raise falcon.HTTPError(falcon.HTTP_404)
        if password is None:
            raise falcon.HTTPError(falcon.HTTP_400, "Can't verify a blank password")
        if user.password is None:
            raise falcon.HTTPError(falcon.HTTP_400, "User has no password set")
        return bcrypt.verify(password, user.password)

    def verify_token(self, token):
        u = _users.first_or_404(verification_token=token)
        u.verified_at = arrow.now().datetime
        u.verification_token = None
        self.save(u)
        return u

    def authenticate(self, data: dict) -> Optional[User]:
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None or password is None:
            return falcon.HTTP_403

        user = _users.first(email=email)
        if _users.verify(user, password):
            return user

        return falcon.HTTP_403

    def gen_token(self, user):
        from smpa.app import auth_backend
        now = arrow.utcnow()
        then = now.shift(hours=24 * 7)
        user_payload = {
            'subject': user.email,
            "issuer": "SmPA",
            "expires_at": str(then),
            "issued_at": str(now),
        }
        return auth_backend.get_auth_token(user_payload)

    def create(self, **kwargs):
        """Creates a user record. Encrypts the password first though and creates a
        linked UserProfile.

        Args:
            **kwargs: Dict of data to create the user.
        """
        kwargs = self._preprocess(**kwargs)
        input_pass = kwargs.pop('password', None)
        if input_pass is None:
            return falcon.HTTP_400

        hashed = self._hash(input_pass)
        kwargs['password'] = hashed
        kwargs['profile_id'] = str(_user_profiles.create().id)
        return super().create(**kwargs)

    def get_or_create(self, **kwargs):
        """Overriden because we need to compare UUIDs to UUIDs and bcrypt can produce
        multiple different hashes for the same password that all magically still verify.

        Args:
            **kwargs: Dict of data to create the user.
        """
        nopass = kwargs.copy()
        nopass.pop('password')
        nopass = self._restore_uuids(**nopass)
        existing_user = self.first(**nopass)
        if existing_user is not None:
            return existing_user

        return self.create(**kwargs)

    def set_password(self, user, password):
        user.password = self._hash(password)
        self.save(user)

    # Private methods

    @staticmethod
    def _hash(password):
        hashed = bcrypt.hash(password)
        return hashed


class AgentService(RService):
    __model__ = Agent


class ApplicantService(RService):
    __model__ = Applicant


class RoleService(RService):
    __model__ = Role


_users = UserService()
_roles = RoleService()
_agents = AgentService()
_applicants = ApplicantService()
