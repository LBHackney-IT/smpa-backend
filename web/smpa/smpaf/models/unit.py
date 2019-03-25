# -*- coding: utf-8 -*-

"""
    models.unit
    ~~~~~~~~~~~
    Unit models.
"""

from .core import BaseModel, ORMMeta2
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType
)

from marshmallow import Schema, fields, pprint


class AreaUnit(Schema, metaclass=ORMMeta2):
    name: str = fields.Str()


class LinearUnit(Schema, metaclass=ORMMeta2):
    name: str = fields.Str()

# class AreaUnit(BaseModel, metaclass=ORMMeta):

#     """Units of measurement of areas. These should populate dropdowns.

#     Attributes:
#         name (TYPE): The name of the unit, eg: sq meters, hectares
#     """
#     name: str = StringType(max_length=100, required=True)


# class LinearUnit(BaseModel, metaclass=ORMMeta):

#     """Units of linear measurement, eg: meters, centimeters, miles

#     Attributes:
#         name (Unicode): The name of the unit.
#     """
#     name = StringType(max_length=100, required=True)
