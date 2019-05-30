# -*- coding: utf-8 -*-

"""
    services.proposal
    ~~~~~~~~~~~~~
    Services for proposal classes
"""

from .rethink import RService

from ..models.proposal import ProposalExtension, ProposalEquipment


class ProposalExtensionService(RService):
    __model__ = ProposalExtension


class ProposalEquipmentService(RService):
    __model__ = ProposalEquipment


_proposals_extension = ProposalExtensionService()
_proposals_equipment = ProposalEquipmentService()
