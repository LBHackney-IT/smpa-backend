# -*- coding: utf-8 -*-

"""
    services.application
    ~~~~~~~~~~~~~~~~
    Planning Application services.
"""

from ..models.application import Application

from .rethink import RService


class ApplicationService(RService):
    __model__ = Application


_applications = ApplicationService()
