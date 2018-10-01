# -*- coding: utf-8 -*-

"""
    models.unit
    ~~~~~~~~~~~
    Unit models.
"""


# 3rd party
import sqlalchemy as sa
from sqlalchemy.ext.associationproxy import association_proxy

# Project
from ..helpers.database import MyUUID

# Module
from .core import BaseModel


class AreaUnit(BaseModel):

    """Units of measurement of areas. These should populate dropdowns.

    Attributes:
        name (TYPE): The name of the unit, eg: sq meters, hectares
    """

    __tablename__ = 'area_units'

    name = sa.Column(sa.Unicode(100))


class LinearUnit(BaseModel):

    """Units of linear measurement, eg: meters, centimeters, miles

    Attributes:
        name (Unicode): The name of the unit.
    """

    __tablename__ = 'linear_units'

    name = sa.Column(sa.Unicode(100))
