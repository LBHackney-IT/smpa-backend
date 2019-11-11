# -*- coding: utf-8 -*-

"""
    services.user
    ~~~~~~~~~~~~~
    User services.
"""

import uuid
import json
import arrow
import falcon
from passlib.hash import bcrypt
from typing import Optional

from smpa.helpers.console import console  # NOQA
from smpa.models.user import Agent, Applicant, Role, User, UserProfile, TelephoneNumberType
from .mongo import DService


class UserProfileService(DService):
    __model__ = UserProfile


_user_profiles = UserProfileService()


class UserService(DService):
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

    def verify_account(self, token):
        u = _users.first(verification_token=token)
        if u is None:
            raise falcon.HTTPError(falcon.HTTP_400, "Invalid verification token")
        elif u.verified is True:
            raise falcon.HTTPError(falcon.HTTP_400, "Account already verified")
        u.verified_at = arrow.utcnow().datetime
        u = self.save(u)
        return u

    def authenticate(self, data: dict) -> Optional[User]:
        email = data.get('email', None)
        password = data.get('password', None)
        user = _users.first(email=email)
        # Check if this user's account is verified
        if user.verified is False:
            raise falcon.HTTPError(falcon.HTTP_401, "Account is not yet verified")

        if email is None or password is None:
            raise falcon.HTTPError(falcon.HTTP_401, "Email or password incomplete")

        if _users.verify(user, password):
            return user

        return falcon.HTTP_401

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
        user = super().create(**kwargs)
        return user

    def register(self, email: str, password: str):
        # Logic for whether we should be allowed to create the user is handled
        # inside resources.auth.SignupResource

        # Create an unvierified account with a verification_token which is used
        # in the account verification step
        from smpa.app import govnotify, config
        vtoken = uuid.uuid4()
        rv = self.create(
            email=email,
            password=password,
            verified_at=None,
            verification_token=vtoken
        )
        vlink = config.get_verification_url(str(vtoken))
        govnotify.send_verify_account(email, vlink)
        return rv

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

        # try getting by id
        existing_user = self.get(kwargs['id'])
        if existing_user is not None:
            return existing_user

        user = self.create(**kwargs)
        return user

    def set_password(self, user, password):
        password = self._hash(password)
        user = self.update(str(user.id), json={'password': password})
        return user

    def verify_passwords(self, password: str, password_confirm: str):
        if password_confirm != password:
            raise falcon.HTTPError(falcon.HTTP_422, 'Passwords do not match')
        elif len(password) < 8:
            raise falcon.HTTPError(falcon.HTTP_422, 'Passwords must be at least 8 characters')

        return True

    # Private methods

    @staticmethod
    def _hash(password):
        hashed = bcrypt.hash(password)
        return hashed


class AgentService(DService):
    __model__ = Agent


class ApplicantService(DService):
    __model__ = Applicant


class RoleService(DService):
    __model__ = Role


class TelephoneNumberTypeService(DService):
    __model__ = TelephoneNumberType


_users = UserService()
_roles = RoleService()
_agents = AgentService()
_applicants = ApplicantService()
_telephone_number_types = TelephoneNumberTypeService()
