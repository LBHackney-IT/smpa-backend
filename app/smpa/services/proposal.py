# -*- coding: utf-8 -*-

"""
    services.proposal
    ~~~~~~~~~~~~~
    Services for proposal classes
"""

from .mongo import DService

from ..models.proposal import ProposalExtension, ProposalEquipment


class ProposalExtensionService(DService):
    __model__ = ProposalExtension


class ProposalEquipmentService(DService):
    __model__ = ProposalEquipment


_proposals_extension = ProposalExtensionService()
_proposals_equipment = ProposalEquipmentService()
