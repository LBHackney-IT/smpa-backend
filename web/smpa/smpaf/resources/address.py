import json
import falcon

from .core import Resource
from ..services.address import (
    _addresses, _site_addresses, _bs7666_addresses, _external_addresses, _international_addresses
)


class AddressResource(Resource):
    _service = _addresses


class SiteAddressResource(Resource):
    _service = _site_addresses


class BS7666AddressResource(Resource):
    _service = _bs7666_addresses


class ExternalAddressResource(Resource):
    _service = _external_addresses


class InternationalAddressResource(Resource):
    _service = _international_addresses

