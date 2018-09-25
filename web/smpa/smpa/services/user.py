# -*- coding: utf-8 -*-

"""
    services.user
    ~~~~~~~~~~~~~
    User services.
"""


class UserService(Service):
    __model__ = User


_users = UserService()
