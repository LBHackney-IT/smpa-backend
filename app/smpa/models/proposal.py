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
    gates_fences_etc: Type['smpa.models.work.WorkExtensionGatesFencesEtc'] = \
        ModelType('smpa.models.work.WorkExtensionGatesFencesEtc')
    means_of_access_to_site: Type['smpa.models.work.WorkExtensionMeansOfAccessToSite'] = \
        ModelType('smpa.models.work.WorkExtensionMeansOfAccessToSite')
    car_bike_spaces: Type['smpa.models.work.WorkExtensionCarBikeSpaces'] = \
        ModelType('smpa.models.work.WorkExtensionCarBikeSpaces')
    basement: Type['smpa.models.work.ExtensionOriginalHouseBasement'] = \
        ModelType('smpa.models.work.ExtensionOriginalHouseBasement')
    roof: Type['smpa.models.work.ExtensionOriginalHouseRoof'] = \
        ModelType('smpa.models.work.ExtensionOriginalHouseRoof')



class ProposalEquipment(WorksProposal):
    pass
