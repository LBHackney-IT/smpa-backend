from molten import field, schema
from typing import Optional, Type
from inspect import Parameter

from ..helpers.console import console

from .core import (
    BaseResource, BaseManager, BaseComponent, make_base_handler, MetaHandler, handler, Handler
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
