# -*- coding: utf-8 -*-

"""
    services.material
    ~~~~~~~~~~~~~~~~~
    Material services.
"""

from .rethink import RService
from ..models.material import (
    MaterialOptionRoof, MaterialOptionWall, MaterialOptionWindow,
    MaterialOptionDoor, BaseMaterial, MaterialRoofOther, MaterialWallOther,
    MaterialWindowOther, MaterialDoorOther, OtherMaterialOther, ExternalBuildingMaterial
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


class MaterialRoofOtherService(RService):
    __model__ = MaterialRoofOther


class MaterialWallOtherService(RService):
    __model__ = MaterialWallOther


class MaterialWindowOtherService(RService):
    __model__ = MaterialWindowOther


class MaterialDoorOtherService(RService):
    __model__ = MaterialDoorOther


class OtherMaterialOtherService(RService):
    __model__ = OtherMaterialOther


class ExternalBuildingMaterialService(RService):
    __model__ = ExternalBuildingMaterial


_material_options_roof = MaterialOptionRoofService()
_material_options_wall = MaterialOptionWallService()
_material_options_window = MaterialOptionWindowService()
_material_options_door = MaterialOptionDoorService()
_base_materials = BaseMaterialService()
_materials_roof_other = MaterialRoofOtherService()
_materials_wall_other = MaterialWallOtherService()
_materials_window_other = MaterialWindowOtherService()
_materials_door_other = MaterialDoorOtherService()
_other_materials = OtherMaterialOtherService()
_external_building_materials = ExternalBuildingMaterialService()
