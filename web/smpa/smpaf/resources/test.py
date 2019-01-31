import json
import falcon

from .core import Resource
from ..services.test import _tests


class TestResource(Resource):
    _service = _tests
