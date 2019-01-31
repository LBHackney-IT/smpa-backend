# -*- coding: utf-8 -*-

"""
    models.site
    ~~~~~~~~~~~
    Planning site related models.
"""

from .core import BaseModel, ORMMeta
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType, ListType, FloatType
)


class SiteArea(BaseModel, metaclass=ORMMeta):

    """Holds info about the area of a site.

    TODO: May refactor this to simply be fields on a Site class depending
    on how other things turn out. Or even fields on a Proposal class.

    Attributes:
        area (float): The number, eg: 20.4
        unit (AreaUnit): The unit that the ``area`` refers to, eg: hactares
    """
    area = FloatType(required=True)
    unit = UUIDType(required=True)  # rel: AreaUnit
