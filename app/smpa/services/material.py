# -*- coding: utf-8 -*-

"""
    services.material
    ~~~~~~~~~~~~~~~~~
    Material services.
"""

from .mongo import DService
from ..models.material import (
    MaterialOptionRoof, MaterialOptionWall, MaterialOptionWindow,
    MaterialOptionDoor, BaseMaterial, MaterialRoof, MaterialWall,
    MaterialWindow, MaterialDoor, OtherMaterial, ExternalBuildingMaterial
)


class MaterialOptionRoofService(DService):
    __model__ = MaterialOptionRoof


class MaterialOptionWallService(DService):
    __model__ = MaterialOptionWall


class MaterialOptionWindowService(DService):
    __model__ = MaterialOptionWindow


class MaterialOptionDoorService(DService):
    __model__ = MaterialOptionDoor


class BaseMaterialService(DService):
    __model__ = BaseMaterial


class MaterialRoofService(DService):
    __model__ = MaterialRoof


class MaterialWallService(DService):
    __model__ = MaterialWall


class MaterialWindowService(DService):
    __model__ = MaterialWindow


class MaterialDoorService(DService):
    __model__ = MaterialDoor


class OtherMaterialService(DService):
    __model__ = OtherMaterial


class ExternalBuildingMaterialService(DService):
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
