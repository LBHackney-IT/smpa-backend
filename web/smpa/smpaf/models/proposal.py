# -*- coding: utf-8 -*-

"""
    models.proposal
    ~~~~~~~~~~~~~~~
    Models for describing a planning proposal.
"""

from .core import BaseModel, ORMMeta
from schematics.types import (  # NOQA
    StringType, BooleanType, DateType, IntType, UUIDType, ListType, FloatType
)


class BaseProposal(BaseModel, metaclass=ORMMeta):

    """The base proposal.

    Attributes:
        site_area_id (UUID): Relationship to SiteArea
        already_completed (bool): Has the project already been completed
        date_completed (TYPE): If so, on what date?
    """

    site_area_id = UUIDType(required=True)
    already_completed = BooleanType(default=False)
    date_completed = DateType()
