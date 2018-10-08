import attr
from molten import field, schema
from typing import Optional
from inspect import Parameter

from ..services.address import AddressService, SiteAddressService
from ..helpers.console import console

from .core import BaseResource, BaseManager, BaseComponent, BaseHandler


@schema
class Address(BaseResource):
    number: Optional[str]
    property_name: Optional[str]
    address_line_1: Optional[str]
    address_line_2: Optional[str]
    address_line_3: Optional[str]
    town_city: Optional[str]
    postcode: Optional[str]


@schema
class SiteAddress(Address):
    postcode: str
    easting: Optional[str]
    northing: Optional[str]
    description: Optional[str]


class AddressManager(BaseManager):
    pass


class SiteAddressManager(BaseManager):
    pass


class AddressManagerComponent(BaseComponent):
    __manager__ = AddressManager
    __service__ = AddressService


class SiteAddressManagerComponent(BaseComponent):
    __manager__ = SiteAddressManager
    __service__ = SiteAddressService


class AddressHandler(BaseHandler):
    __resource__ = Address
    __manager__ = AddressManager
    __namespace__ = 'addresses'


class SiteAddressHandler(BaseHandler):
    __resource__ = SiteAddress
    __manager__ = SiteAddressManager
    __namespace__ = 'site_addresses'
