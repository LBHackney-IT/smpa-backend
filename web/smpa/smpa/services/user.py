# -*- coding: utf-8 -*-

"""
    services.user
    ~~~~~~~~~~~~~
    User services.
"""

from ..models import User

from .core import Service


class UserService(Service):
    __model__ = User


_users = UserService()
