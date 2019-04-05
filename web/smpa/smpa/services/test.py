# -*- coding: utf-8 -*-

"""
    services.test
    ~~~~~~~~~~~~~
    Test service.
"""

from .rethink import RService

from ..models.test import Test


class TestService(RService):
    __model__ = Test


_tests = TestService()
