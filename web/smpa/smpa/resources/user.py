from molten import field, schema
from typing import Optional, Type
from inspect import Parameter

from ..services.user import AgentService, ApplicantService
from ..helpers.console import console  # NOQA

from .core import (
    BaseResource, BaseManager, BaseComponent, MetaHandler
)
from .address import Address


@schema
class Email(BaseResource):
    email_address: str
    verified: bool


@schema
class TelephoneNumberType(BaseResource):
    name: str


@schema
class TelephoneNumber(BaseResource):
    tel_number: str
    tel_type: Type[TelephoneNumberType]


@schema
class PersonName(BaseResource):
    title: Optional[str]
    given_name: Optional[str]
    family_name: str


@schema
class Person(BaseResource):
    person_name: Type[PersonName]
    company_name: Optional[str]
    address: Type[Address]

    primary_number: Type[TelephoneNumber]
    secondary_number: Optional[Type[TelephoneNumber]]
    fax_number: Optional[Type[TelephoneNumber]]
    email_address: Type[Email]


@schema
class Applicant(Person):
    pass


@schema
class Agent(Person):
    pass


class AgentManager(BaseManager):
    _service: AgentService


class ApplicantManager(BaseManager):
    _service: ApplicantService


class AgentManagerComponent(BaseComponent):
    __manager__ = AgentManager
    __service__ = AgentService
    __resource__: Agent


class ApplicantManagerComponent(BaseComponent):
    __manager__ = ApplicantManager
    __service__ = ApplicantService
    __resource__: Applicant


class AgentHandler(metaclass=MetaHandler):
    resource: Type[Agent] = Agent
    manager: Type[AgentManager] = AgentManager
    namespace: str = 'addresses'


class ApplicantHandler(metaclass=MetaHandler):
    resource: Type[Applicant] = Applicant
    manager: Type[ApplicantManager] = ApplicantManager
    namespace: str = 'applicants'
