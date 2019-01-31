# -*- coding: utf-8 -*-

"""
    services.address
    ~~~~~~~~~~~~~~~~
    Address services.
"""

from ..models.address import (
    Address, SiteAddress, BS7666Address, InternationalAddress, ExternalAddress
)

from .core import Service


class AddressService(Service):
    __model__ = Address


class SiteAddressService(Service):
    __model__ = SiteAddress


class BS7666AddressService(Service):
    __model__ = BS7666Address


class ExternalAddressService(Service):
    __model__ = ExternalAddress


class InternationalAddressService(Service):
    __model__ = InternationalAddress


_addresses = AddressService()
_site_addresses = SiteAddressService()
_bs7666_addresses = BS7666AddressService()
_external_addresses = ExternalAddressService()
_international_addresses = InternationalAddressService()
