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


class SiteConstraints(BaseModel, metaclass=ORMMeta):

    """Planning constraints on the site. These field names come from the
    geoserver.
    """
    has_boundary: str = StringType()
    nb_a4d: int = IntType()
    a4d_name: str = StringType()
    nb_conarea: int = IntType()
    conarea_name: str = StringType()
    nb_tpo: int = IntType()
    tpo_name: str = StringType()
    is_listed_building: str = StringType()
    is_floodzone_2: str = StringType()
    is_floodzone_3a: str = StringType()
    is_floodzone_3b: str = StringType()
    geom: str = StringType()  # JSON blob
    uprn: int = IntType()

    # See backrefs on Application
    application_id: str = UUIDType()
