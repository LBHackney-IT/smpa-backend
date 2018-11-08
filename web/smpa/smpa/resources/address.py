import attr
from molten import field, schema
from typing import Optional, Type
from inspect import Parameter

from ..services.address import AddressService, SiteAddressService
from ..helpers.console import console

from .core import (
    BaseResource, BaseManager, BaseComponent, make_base_handler, MetaHandler, handler, Handler
)


@schema
class Address:
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
    _service: AddressService


class SiteAddressManager(BaseManager):
    _service: SiteAddressService


class AddressManagerComponent(BaseComponent):
    __manager__ = AddressManager
    __service__ = AddressService
    __resource__: Address


class SiteAddressManagerComponent(BaseComponent):
    __manager__ = SiteAddressManager
    __service__ = SiteAddressService
    __resource__: SiteAddress


class AddressHandler(metaclass=MetaHandler):
    resource: Type[Address] = Address
    manager: Type[AddressManager] = AddressManager
    namespace: str = 'addresses'


class SiteAddressHandler(metaclass=MetaHandler):
    resource: Type[SiteAddress] = SiteAddress
    manager: Type[SiteAddressManager] = SiteAddressManager
    namespace: str = 'site_addresses'


# @handler(Address, AddressManager, 'addresses')
# class AddressHandler:
#     pass


# @handler(SiteAddress, SiteAddressManager, 'site_addresses')
# class SiteAddressHandler:
#     pass


# @Handler(Address, AddressManager, 'addresses')
# class AddressHandler:
#     pass


# @Handler(SiteAddress, SiteAddressManager, 'site_addresses')
# class SiteAddressHandler:
#     pass


# class AddressHandler(make_base_handler(Address, AddressManager, 'addresses')):
#     pass


# class SiteAddressHandler(make_base_handler(SiteAddress, SiteAddressManager, 'site_addresses')):
#     pass
