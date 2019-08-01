# -*- coding: utf-8 -*-

"""
    services.unit
    ~~~~~~~~~~~~~
    Services for units of measurement.
"""

from .mongo import DService

from ..models.unit import AreaUnit, LinearUnit


class AreaUnitService(DService):
    __model__ = AreaUnit


class LinearUnitService(DService):
    __model__ = LinearUnit


_area_units = AreaUnitService()
_linear_units = LinearUnitService()
