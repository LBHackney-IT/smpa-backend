# -*- coding: utf-8 -*-

"""
    services.work
    ~~~~~~~~~~~~~
    Works services.
"""

from ..models.work import (
    WorksLocation, BasementWorksLocation
)

from .rethink import RService


class WorksLocationService(RService):
    __model__ = WorksLocation


_works_locations = WorksLocationService()


class BasementWorksLocationService(RService):
    __model__ = BasementWorksLocation


_basement_works_locations = BasementWorksLocationService()
