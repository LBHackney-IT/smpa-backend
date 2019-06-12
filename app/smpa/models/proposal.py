# -*- coding: utf-8 -*-

"""
    models.proposal
    ~~~~~~~~~~~~~~~
    Models for describing a planning proposal.
"""

from .core import BaseModel, ORMMeta
from typing import Type
from schematics.types import (  # NOQA
    StringType, BooleanType, DateType, IntType, UUIDType, ListType, FloatType, ModelType
)


class WorksProposal(BaseModel, metaclass=ORMMeta):

    """The base proposal.
    """
    application_id: str = UUIDType()


class ProposalExtension(WorksProposal):

    """Summary
    """
    original_house: Type['smpa.models.work.WorkExtensionOriginalHouse'] = \
        ModelType('smpa.models.work.WorkExtensionOriginalHouse')
    incidental_buildings: Type['smpa.models.work.WorkExtensionIncidentalBuildings'] = \
        ModelType('smpa.models.work.WorkExtensionIncidentalBuildings')
    boundaries: Type['smpa.models.work.WorkExtensionBoundaries'] = \
        ModelType('smpa.models.work.WorkExtensionBoundaries')
    means_of_access: Type['smpa.models.work.WorkExtensionMeansOfAccess'] = \
        ModelType('smpa.models.work.WorkExtensionMeansOfAccess')
    parking: Type['smpa.models.work.WorkExtensionParking'] = \
        ModelType('smpa.models.work.WorkExtensionParking')
    trees: Type['smpa.models.work.WorkTrees'] = \
        ModelType('smpa.models.work.WorkTrees')


    additional_floor_area = FloatType()
    additional_floor_area_units_id = UUIDType()

    new_single_bedrooms = IntType()
    new_double_bedrooms = IntType()


class ProposalEquipment(WorksProposal):
    equipment: Type['smpa.models.work.WorkEquipment'] = \
        ModelType('smpa.models.work.WorkEquipment')
