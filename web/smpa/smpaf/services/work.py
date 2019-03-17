# -*- coding: utf-8 -*-

"""
    services.work
    ~~~~~~~~~~~~~
    Works services.
"""

from ..models.work import (
    WorksLocation
)

from .rethink import RService


class WorksLocationService(RService):
    __model__ = WorksLocation


_works_locations = WorksLocationService()
