from molten import field, schema
from typing import Optional
from inspect import Parameter

from ..services.address import AddressService, _addresses
from ..helpers.console import console

from .core import BaseResource


@schema
class Address(BaseResource):
    number: Optional[str]
    property_name: Optional[str]
    address_line_1: Optional[str]
    address_line_2: Optional[str]
    address_line_3: Optional[str]
    town_city: Optional[str]
    postcode: Optional[str]


class AddressManagerComponent:
    is_cacheable = True
    is_singleton = True

    def can_handle_parameter(self, parameter: Parameter) -> bool:
        return parameter.annotation is AddressService

    def resolve(self) -> AddressService:
        return _addresses


def create_address(address: Address, address_manager: AddressService) -> Address:
    console.info(address)
    return address_manager.create(address)
