# -*- coding: utf-8 -*-

"""
    services.unit
    ~~~~~~~~~~~~~
    Services for units of measurement.
"""

from .rethink import RService

from ..models.unit import AreaUnit, LinearUnit


class AreaUnitService(RService):
    __model__ = AreaUnit


class LinearUnitService(RService):
    __model__ = LinearUnit


_area_units = AreaUnitService()
_linear_units = LinearUnitService()
