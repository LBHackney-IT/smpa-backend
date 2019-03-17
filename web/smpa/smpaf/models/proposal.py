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


class WorksProposal(BaseModel, metaclass=ORMMeta):

    """The base proposal.

    Attributes:
        site_area_id (UUID): Relationship to SiteArea
    """
    pass


class ExtensionProposal(WorksProposal):

    """Summary
    """

    # original_house
    # incidental_buildings
    # gates_fences_etc
    # means_of_access_to_site
    # car_bike_spaces


class EquipmentProposal(WorksProposal):
    pass
