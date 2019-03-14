import json
import falcon

from .core import Resource
from ..services.unit import _area_units, _linear_units


class AreaUnitResource(Resource):
    _service = _area_units
    auth = {
        'exempt_methods': ['GET']
    }


class LinearUnitResource(Resource):
    _service = _linear_units
    auth = {
        'exempt_methods': ['GET']
    }
