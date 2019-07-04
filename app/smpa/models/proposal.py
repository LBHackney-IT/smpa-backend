# -*- coding: utf-8 -*-

"""
    models.proposal
    ~~~~~~~~~~~~~~~
    Models for describing a planning proposal.
"""

from .core import BaseModel, ORMMeta, RelType
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

    materials: Type['smpa.models.material.MaterialExtension'] = \
        ModelType('smpa.models.material.MaterialExtension')

    additional_floor_area = FloatType()
    additional_floor_area_units_id = RelType(
        UUIDType(),
        to_field='additional_floor_area_units',
        service='AreaUnitService'
    )
    additional_floor_area_units = ModelType('smpa.models.unit.AreaUnit')

    new_single_bedrooms = IntType()
    new_double_bedrooms = IntType()

    owner_id = RelType(
        UUIDType(),
        to_field='owner',
        service='UserService'
    )
    owner: Type['smpa.models.user.User'] = ModelType('smpa.models.user.User')


class ProposalEquipment(WorksProposal):
    equipment: Type['smpa.models.work.WorkEquipment'] = \
        ModelType('smpa.models.work.WorkEquipment')

    owner_id = RelType(
        UUIDType(),
        to_field='owner',
        service='UserService'
    )
    owner: Type['smpa.models.user.User'] = ModelType('smpa.models.user.User')
