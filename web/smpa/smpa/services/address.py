# -*- coding: utf-8 -*-

"""
    services.address
    ~~~~~~~~~~~~~~~~
    Address services.
"""

from ..models.address import Address

from .core import Service


class AddressService(Service):
    __model__ = Address


_addresses = AddressService()
