# -*- coding: utf-8 -*-

"""
    services.tmp
    ~~~~~~~~~~~~
    Services for testing models and services.
"""

from .mongo import DService

from smpa.models.tmp import TempModel


class TempModelService(DService):
    __model__ = TempModel


_temp_models = TempModelService()
