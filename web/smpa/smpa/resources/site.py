from molten import field, schema
from typing import Optional, Type
from inspect import Parameter
from arrow.arrow import Arrow

from ..helpers.console import console

from .core import (
    BaseResource, BaseManager, BaseComponent, make_base_handler, MetaHandler, handler, Handler
)

from .unit import Area


@schema
class SiteArea(Area):
    pass


@schema
class ExistingUseContamination(BaseResource):
    known: bool
    suspected: bool
    proposal_vulnerable: bool


@schema
class ExistingUse(BaseResource):
    description: str
    vacant: bool
    last_use: str
    last_use_end: Optional[Arrow]
    contaminations: Type[ExistingUseContamination]


@schema
class SiteOwnership(BaseResource):
    owned_by_applicant: bool
    owners_notified: bool
    # owners_details: str


@schema
class Site(BaseResource):
    area: Type[SiteArea]
    current_use: Type[ExistingUse]
    ownership: Type[SiteOwnership]
