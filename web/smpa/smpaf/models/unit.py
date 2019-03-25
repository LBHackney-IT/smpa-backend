# -*- coding: utf-8 -*-

"""
    models.unit
    ~~~~~~~~~~~
    Unit models.
"""

from .core import BaseModel, ORMMeta
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType
)

from marshmallow import fields, validate, pprint  # NOQA


class AreaUnit(BaseModel, metaclass=ORMMeta):
    name: str = fields.Str(validate=validate.Length(max=100), required=True)


class LinearUnit(BaseModel, metaclass=ORMMeta):
    name: str = fields.Str(validate=validate.Length(max=100), required=True)

# class AreaUnit(BaseModel, metaclass=ORMMeta):

#     """Units of measurement of areas. These should populate dropdowns.

#     Attributes:
#         name (TYPE): The name of the unit, eg: sq meters, hectares
#     """
#     name: str = fields.Str(validate=validate.Length(max=100), required=True)


# class LinearUnit(BaseModel, metaclass=ORMMeta):

#     """Units of linear measurement, eg: meters, centimeters, miles

#     Attributes:
#         name (Unicode): The name of the unit.
#     """
#     name = fields.Str(validate=validate.Length(max=100), required=True)
