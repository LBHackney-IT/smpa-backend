import json
import falcon

from .core import Resource
from ..services.material import (
    _material_options_roof, _material_options_wall, _material_options_window,
    _material_options_door, _base_materials, _materials_roof, _materials_wall, _materials_window,
    _materials_door, _other_materials, _external_building_materials
)


class MaterialOptionRoofResource(Resource):
    _service = _material_options_roof
    auth = {
        'exempt_methods': ['GET']
    }


class MaterialOptionWallResource(Resource):
    _service = _material_options_wall
    auth = {
        'exempt_methods': ['GET']
    }


class MaterialOptionWindowResource(Resource):
    _service = _material_options_window
    auth = {
        'exempt_methods': ['GET']
    }


class MaterialOptionDoorResource(Resource):
    _service = _material_options_door
    auth = {
        'exempt_methods': ['GET']
    }
