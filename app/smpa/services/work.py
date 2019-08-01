# -*- coding: utf-8 -*-

"""
    services.work
    ~~~~~~~~~~~~~
    Works services.
"""

from ..models.work import (
    WorksLocation,
    BasementWorksType,
    RoofWorksType,
    BorderWorksType,
    AccessWorksScope,
    AccessWorksType,
    ParkingWorksScope,
    EquipmentWorksType,
    EquipmentWorksConservationType,
    WorkExtensionOption,
    ExtensionOriginalHouseSingleStoreyExtension,
    ExtensionOriginalHouseTwoStoreyExtension,
    ExtensionOriginalHousePartSinglePartTwoStoreyExtension,
    ExtensionOriginalHouseBasement,
    ExtensionOriginalHouseRoof,
    ExtensionOutbuilding,
    ExtensionOriginalHousePorch,
    ExtensionOriginalHouseBalconyTerrace,
    ExtensionOriginalHouseStaircase,
    ExtensionOriginalHouseWindowsDoors,
    ExtensionOriginalHouseCladding,
    Work,
    WorkExtensionOriginalHouse,
    WorkExtensionIncidentalBuildings,
    WorkExtensionBoundaries,
    WorkExtensionMeansOfAccess,
    WorkExtensionParking,
    WorkEquipment,
    WorkTrees,
    GatesFencesWallsType,
)

from .mongo import DService


class WorksLocationService(DService):
    __model__ = WorksLocation


class BasementWorksTypeService(DService):
    __model__ = BasementWorksType


class RoofWorksTypeService(DService):
    __model__ = RoofWorksType


class BorderWorksTypeService(DService):
    __model__ = BorderWorksType


class AccessWorksScopeService(DService):
    __model__ = AccessWorksScope


class AccessWorksTypeService(DService):
    __model__ = AccessWorksType


class ParkingWorksScopeService(DService):
    __model__ = ParkingWorksScope


class EquipmentWorksTypeService(DService):
    __model__ = EquipmentWorksType


class EquipmentWorksConservationTypeService(DService):
    __model__ = EquipmentWorksConservationType


class WorkExtensionOptionService(DService):
    __model__ = WorkExtensionOption


class ExtensionOriginalHouseSingleStoreyExtensionService(DService):
    __model__ = ExtensionOriginalHouseSingleStoreyExtension


class ExtensionOriginalHouseTwoStoreyExtensionService(DService):
    __model__ = ExtensionOriginalHouseTwoStoreyExtension


class ExtensionOriginalHousePartSinglePartTwoStoreyExtensionService(DService):
    __model__ = ExtensionOriginalHousePartSinglePartTwoStoreyExtension


class ExtensionOriginalHouseBasementService(DService):
    __model__ = ExtensionOriginalHouseBasement


class ExtensionOriginalHouseRoofService(DService):
    __model__ = ExtensionOriginalHouseRoof


class ExtensionOutbuildingService(DService):
    __model__ = ExtensionOutbuilding


class ExtensionOriginalHousePorchService(DService):
    __model__ = ExtensionOriginalHousePorch


class ExtensionOriginalHouseBalconyTerraceService(DService):
    __model__ = ExtensionOriginalHouseBalconyTerrace


class ExtensionOriginalHouseStaircaseService(DService):
    __model__ = ExtensionOriginalHouseStaircase


class ExtensionOriginalHouseWindowsDoorsService(DService):
    __model__ = ExtensionOriginalHouseWindowsDoors


class ExtensionOriginalHouseCladdingService(DService):
    __model__ = ExtensionOriginalHouseCladding


class WorkService(DService):
    __model__ = Work


class WorkExtensionOriginalHouseService(DService):
    __model__ = WorkExtensionOriginalHouse


class WorkExtensionIncidentalBuildingsService(DService):
    __model__ = WorkExtensionIncidentalBuildings


class WorkExtensionBoundariesService(DService):
    __model__ = WorkExtensionBoundaries


class WorkExtensionMeansOfAccessService(DService):
    __model__ = WorkExtensionMeansOfAccess


class WorkExtensionParkingService(DService):
    __model__ = WorkExtensionParking


class WorkEquipmentService(DService):
    __model__ = WorkEquipment


class WorkTreesService(DService):
    __model__ = WorkTrees


class GatesFencesWallsTypeService(DService):
    __model__ = GatesFencesWallsType


_works_locations = WorksLocationService()
_basement_works_types = BasementWorksTypeService()
_roof_works_types = RoofWorksTypeService()
_border_works_types = BorderWorksTypeService()
_access_works_scopes = AccessWorksScopeService()
_access_works_types = AccessWorksTypeService()
_parking_works_scopes = ParkingWorksScopeService()
_equipment_works_types = EquipmentWorksTypeService()
_equipment_works_conservation_types = EquipmentWorksConservationTypeService()
_work_extension_options = WorkExtensionOptionService()
_gates_fences_walls_types = GatesFencesWallsTypeService()

_extension_original_house_single_storey_extensions = \
    ExtensionOriginalHouseSingleStoreyExtensionService()
_extension_original_house_two_storey_extensions = \
    ExtensionOriginalHouseTwoStoreyExtensionService()
_extension_original_house_part_single_part_two_storey_extensions = \
    ExtensionOriginalHousePartSinglePartTwoStoreyExtensionService()
_extension_original_house_basements = ExtensionOriginalHouseBasementService()
_extension_original_house_roofs = ExtensionOriginalHouseRoofService()
_extension_outbuildings = ExtensionOutbuildingService()
_extension_original_house_porchs = ExtensionOriginalHousePorchService()
_extension_original_house_balcony_terraces = ExtensionOriginalHouseBalconyTerraceService()
_extension_original_house_staircases = ExtensionOriginalHouseStaircaseService()
_extension_original_house_add_replacement_windows_doors = \
    ExtensionOriginalHouseWindowsDoorsService()
_extension_original_house_claddings = ExtensionOriginalHouseCladdingService()
_works = WorkService()
_work_extension_original_houses = WorkExtensionOriginalHouseService()
_work_extension_incidental_buildings = WorkExtensionIncidentalBuildingsService()
_work_extension_boundaries = WorkExtensionBoundariesService()
_work_extension_means_of_access_to_sites = WorkExtensionMeansOfAccessService()
_work_extension_car_bike_spaces = WorkExtensionParkingService()
_work_equipments = WorkEquipmentService()
_work_trees = WorkTreesService()
