# -*- coding: utf-8 -*-

"""
    models.application
    ~~~~~~~~~~~~~~~~~~
    Application is our root model. Everything else is part of this.
"""

from .core import BaseModel, ORMMeta, RelType
from typing import Type
from datetime import date
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType, ListType,
    FloatType, ModelType, DateType
)

from .user import User
# from .address import SiteAddress


class Application(BaseModel, metaclass=ORMMeta):

    # First screen when starting a new application
    works_started: bool = BooleanType(default=False)
    date_works_started: date = DateType()
    works_completed: bool = BooleanType(default=False)
    date_works_completed: date = DateType()
    works_description: str = StringType()

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
