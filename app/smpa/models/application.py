# -*- coding: utf-8 -*-

"""
    models.application
    ~~~~~~~~~~~~~~~~~~
    Application is our root model. Everything else is part of this.
"""

from .core import BaseModel, ORMMeta, RelType
from typing import Type, List
from datetime import date
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType, ListType,
    FloatType, ModelType, DateType
)

from .user import User
from .meta import Declaration, OwnershipType
# from .address import SiteAddress


class Application(BaseModel, metaclass=ORMMeta):

    # First screen when starting a new application
    works_started: bool = BooleanType(default=False)
    date_works_started: date = DateType()
    works_completed: bool = BooleanType(default=False)
    date_works_completed: date = DateType()
    works_description: str = StringType()

    free_text_description: str = StringType()
    ownership_declaration = BooleanType(default=False)
    reduction_eligible = BooleanType(default=False)

    # This is Ana's Application state
    proposalFlow: str = StringType()

    declaration_id = RelType(
        UUIDType(),
        to_field='declaration',
        service='DeclarationService'
    )
    declaration: Type[Declaration] = ModelType(Declaration)

    ownership_type_id = RelType(
        UUIDType(),
        to_field='ownership_type',
        service='OwnershipTypeService'
    )
    ownership_type: Type[OwnershipType] = ModelType(OwnershipType)

    owner_id = RelType(
        UUIDType(),
        to_field='owner',
        service='UserService'
    )
    owner: Type[User] = ModelType(User)

    #
    # Dynamic relations
    #

    backrefs = [
        ('application_id', 'SiteAddressService'),
        ('application_id', 'SiteConstraintsService'),
        ('application_id', 'ProposalExtensionService'),
        ('application_id', 'ProposalEquipmentService'),
    ]
    site_address: Type['smpa.models.address.SiteAddress'] = \
        ModelType('smpa.models.address.SiteAddress')
    site_constraints: Type['smpa.models.site.SiteConstraints'] = \
        ModelType('smpa.models.site.SiteConstraints')
    proposal_extension: Type['smpa.models.proposal.ProposalExtension'] = \
        ModelType('smpa.models.proposal.ProposalExtension')
    proposal_equipment: Type['smpa.models.proposal.ProposalEquipment'] = \
        ModelType('smpa.models.proposal.ProposalEquipment')

    list_backrefs = [
        ('application_id', 'DocumentFileService', 'document_files'),
        ('application_id', 'PaymentService', 'payments'),
    ]
    document_files: List[Type['smpa.models.document.DocumentFile']] = \
        ListType(ModelType('smpa.models.document.DocumentFile'))
    payments: List[Type['smpa.models.payment.Payment']] = \
        ListType(ModelType('smpa.models.payment.Payment'))
