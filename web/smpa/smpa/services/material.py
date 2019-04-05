# -*- coding: utf-8 -*-

"""
    services.material
    ~~~~~~~~~~~~~~~~~
    Material services.
"""

from .rethink import RService
from ..models.material import (
    MaterialOptionRoof, MaterialOptionWall, MaterialOptionWindow,
    MaterialOptionDoor, BaseMaterial, MaterialRoof, MaterialWall,
    MaterialWindow, MaterialDoor, OtherMaterial, ExternalBuildingMaterial
)


class MaterialOptionRoofService(RService):
    __model__ = MaterialOptionRoof


class MaterialOptionWallService(RService):
    __model__ = MaterialOptionWall


class MaterialOptionWindowService(RService):
    __model__ = MaterialOptionWindow


class MaterialOptionDoorService(RService):
    __model__ = MaterialOptionDoor


class BaseMaterialService(RService):
    __model__ = BaseMaterial


class MaterialRoofService(RService):
    __model__ = MaterialRoof


class MaterialWallService(RService):
    __model__ = MaterialWall


class MaterialWindowService(RService):
    __model__ = MaterialWindow


class MaterialDoorService(RService):
    __model__ = MaterialDoor


class OtherMaterialService(RService):
    __model__ = OtherMaterial


class ExternalBuildingMaterialService(RService):
    __model__ = ExternalBuildingMaterial


_material_options_roof = MaterialOptionRoofService()
_material_options_wall = MaterialOptionWallService()
_material_options_window = MaterialOptionWindowService()
_material_options_door = MaterialOptionDoorService()
_base_materials = BaseMaterialService()
_materials_roof = MaterialRoofService()
_materials_wall = MaterialWallService()
_materials_window = MaterialWindowService()
_materials_door = MaterialDoorService()
_other_materials = OtherMaterialService()
_external_building_materials = ExternalBuildingMaterialService()
