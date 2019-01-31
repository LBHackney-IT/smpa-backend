# -*- coding: utf-8 -*-

"""
    models.site
    ~~~~~~~~~~~
    Planning site related models.
"""


# 3rd party
import sqlalchemy as sa
from sqlalchemy.ext.associationproxy import association_proxy

# Project
from ..helpers.database import MyUUID

# Module
from .core import BaseModel


class SiteArea(BaseModel):

    """Holds info about the area of a site.

    TODO: May refactor this to simply be fields on a Site class depending
    on how other things turn out. Or even fields on a Proposal class.

    Attributes:
        area (float): The number, eg: 20.4
        unit (AreaUnit): The unit that the ``area`` refers to, eg: hactares
    """

    __tablename__ = 'site_areas'

    area = sa.Column(sa.Float(), nullable=False)
    unit = sa.Column(MyUUID, sa.ForeignKey('area_units.id'))
