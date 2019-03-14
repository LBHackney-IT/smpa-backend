# -*- coding: utf-8 -*-

"""
    services.user
    ~~~~~~~~~~~~~
    User services.
"""

import falcon
from passlib.hash import bcrypt
from ..models import User, Agent, Applicant

from .core import Service


class UserService(Service):
    __model__ = User

    def _hash(self, password):
        hashed = bcrypt.hash(password)
        return hashed

    def verify(self, user, password):
        return bcrypt.verify(password, user.password)

    def create(self, **kwargs):
        """Creates a user record. Encrypts the password first though.

        Args:
            **kwargs: Dict of data to create the user.
        """
        input_pass = kwargs.pop('password', None)
        if input_pass is None:
            return falcon.HTTP_403

        hashed = self._hash(input_pass)
        kwargs['password'] = hashed
        return super().create(**kwargs)


class AgentService(Service):
    __model__ = Agent


class ApplicantService(Service):
    __model__ = Applicant


_users = UserService()
_agents = AgentService()
_applicants = ApplicantService()
