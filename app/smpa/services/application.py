# -*- coding: utf-8 -*-

"""
    services.application
    ~~~~~~~~~~~~~~~~
    Planning Application services.
"""

from ..models.application import Application

from .mongo import DService


class ApplicationService(DService):
    __model__ = Application


_applications = ApplicationService()
