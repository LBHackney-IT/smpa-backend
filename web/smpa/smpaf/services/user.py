# -*- coding: utf-8 -*-

"""
    services.user
    ~~~~~~~~~~~~~
    User services.
"""

import falcon
from passlib.hash import bcrypt
from ..models.user import Role, User, Agent, Applicant, UserProfile

from .rethink import RService


class UserProfileService(RService):
    __model__ = UserProfile


_user_profiles = UserProfileService()


class UserService(RService):
    __model__ = User

    def _hash(self, password):
        hashed = bcrypt.hash(password)
        return hashed

    def verify(self, user, password):
        return bcrypt.verify(password, user.password)

    def create(self, **kwargs):
        """Creates a user record. Encrypts the password first though and creates a
        linked UserProfile.

        Args:
            **kwargs: Dict of data to create the user.
        """
        input_pass = kwargs.pop('password', None)
        if input_pass is None:
            return falcon.HTTP_403

        hashed = self._hash(input_pass)
        kwargs['password'] = hashed
        kwargs['profile_id'] = str(_user_profiles.create().id)
        return super().create(**kwargs)


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
