from molten import field, schema
from typing import Optional, Type
from inspect import Parameter
from arrow.arrow import Arrow

from ..helpers.database import MyUUID
from ..helpers.console import console
from ..services.application import PlanningApplicationService

from .user import Applicant, Agent
from .development import Proposal
from .site import Site
from .core import (
    BaseResource, BaseManager, BaseComponent, MetaHandler, make_base_handler
)


@schema
class Declaration(BaseResource):
    is_staff_member: bool
    is_elected_member: bool
    is_staff_related: bool
    is_elected_related: bool


@schema
class PlanningApplication:
    """This is probably going to be the top of the schema tree for
    a new planning application.
    """
    id: Optional[MyUUID] = field(response_only=True)
    created_at: Optional[Arrow]
    updated_at: Optional[Arrow]
    #
    applicant: Type[Applicant]
    agent: Type[Agent]
    proposal: Type[Proposal]
    declaration: Type[Declaration]
    site: Type[Site]


class PlanningApplicationManager(BaseManager):
    _service = PlanningApplicationService


class PlanningApplicationManagerComponent(BaseComponent):
    __manager__ = PlanningApplicationManager
    __service__ = PlanningApplicationService
    __resource__ = PlanningApplication


class PlanningApplicationHandler(metaclass=MetaHandler):
    resource: Type[PlanningApplication] = PlanningApplication
    manager: Type[PlanningApplicationManager] = PlanningApplicationManager
    namespace: str = 'planning_applications'
