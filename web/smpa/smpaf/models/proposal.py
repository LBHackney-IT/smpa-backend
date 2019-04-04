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
    original_house: Type['smpaf.models.work.WorkExtensionOriginalHouse'] = \
        ModelType('smpaf.models.work.WorkExtensionOriginalHouse')
    incidental_buildings: Type['smpaf.models.work.WorkExtensionIncidentalBuildings'] = \
        ModelType('smpaf.models.work.WorkExtensionIncidentalBuildings')
    gates_fences_etc: Type['smpaf.models.work.WorkExtensionGatesFencesEtc'] = \
        ModelType('smpaf.models.work.WorkExtensionGatesFencesEtc')
    means_of_access_to_site: Type['smpaf.models.work.WorkExtensionMeansOfAccessToSite'] = \
        ModelType('smpaf.models.work.WorkExtensionMeansOfAccessToSite')
    car_bike_spaces: Type['smpaf.models.work.WorkExtensionCarBikeSpaces'] = \
        ModelType('smpaf.models.work.WorkExtensionCarBikeSpaces')


class ProposalEquipment(WorksProposal):
    pass
