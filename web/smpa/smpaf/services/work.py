# -*- coding: utf-8 -*-

"""
    services.work
    ~~~~~~~~~~~~~
    Works services.
"""

from ..models.work import (
    WorksLocation,
    BasementWorksLocation,
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
    ExtensionOriginalHouseRoofWorks,
    ExtensionOriginalHouseOutbuilding,
    ExtensionOriginalHousePorch,
    ExtensionOriginalHouseBalconyTerrace,
    ExtensionOriginalHouseStaircase,
    ExtensionOriginalHouseAddReplacementWindowsDoors,
    ExtensionOriginalHouseCladding,
    Work,
    WorkExtensionOriginalHouse,
    WorkExtensionIncidentalBuildings,
    WorkExtensionGatesFencesEtc,
    WorkExtensionMeansOfAccessToSite,
    WorkExtensionCarBikeSpaces,
    WorkEquipment,
    WorkTrees,
)

from .rethink import RService


class WorksLocationService(RService):
    __model__ = WorksLocation


class BasementWorksLocationService(RService):
    __model__ = BasementWorksLocation


class RoofWorksTypeService(RService):
    __model__ = RoofWorksType


class BorderWorksTypeService(RService):
    __model__ = BorderWorksType


class AccessWorksScopeService(RService):
    __model__ = AccessWorksScope


class AccessWorksTypeService(RService):
    __model__ = AccessWorksType


class ParkingWorksScopeService(RService):
    __model__ = ParkingWorksScope


class EquipmentWorksTypeService(RService):
    __model__ = EquipmentWorksType


class EquipmentWorksConservationTypeService(RService):
    __model__ = EquipmentWorksConservationType


class WorkExtensionOptionService(RService):
    __model__ = WorkExtensionOption


class ExtensionOriginalHouseSingleStoreyExtensionService(RService):
    __model__ = ExtensionOriginalHouseSingleStoreyExtension


class ExtensionOriginalHouseTwoStoreyExtensionService(RService):
    __model__ = ExtensionOriginalHouseTwoStoreyExtension


class ExtensionOriginalHousePartSinglePartTwoStoreyExtensionService(RService):
    __model__ = ExtensionOriginalHousePartSinglePartTwoStoreyExtension


class ExtensionOriginalHouseBasementService(RService):
    __model__ = ExtensionOriginalHouseBasement


class ExtensionOriginalHouseRoofWorksService(RService):
    __model__ = ExtensionOriginalHouseRoofWorks


class ExtensionOriginalHouseOutbuildingService(RService):
    __model__ = ExtensionOriginalHouseOutbuilding


class ExtensionOriginalHousePorchService(RService):
    __model__ = ExtensionOriginalHousePorch


class ExtensionOriginalHouseBalconyTerraceService(RService):
    __model__ = ExtensionOriginalHouseBalconyTerrace


class ExtensionOriginalHouseStaircaseService(RService):
    __model__ = ExtensionOriginalHouseStaircase


class ExtensionOriginalHouseAddReplacementWindowsDoorsService(RService):
    __model__ = ExtensionOriginalHouseAddReplacementWindowsDoors


class ExtensionOriginalHouseCladdingService(RService):
    __model__ = ExtensionOriginalHouseCladding


class WorkService(RService):
    __model__ = Work


class WorkExtensionOriginalHouseService(RService):
    __model__ = WorkExtensionOriginalHouse


class WorkExtensionIncidentalBuildingsService(RService):
    __model__ = WorkExtensionIncidentalBuildings


class WorkExtensionGatesFencesEtcService(RService):
    __model__ = WorkExtensionGatesFencesEtc


class WorkExtensionMeansOfAccessToSiteService(RService):
    __model__ = WorkExtensionMeansOfAccessToSite


class WorkExtensionCarBikeSpacesService(RService):
    __model__ = WorkExtensionCarBikeSpaces


class WorkEquipmentService(RService):
    __model__ = WorkEquipment


class WorkTreesService(RService):
    __model__ = WorkTrees


_works_locations = WorksLocationService()
_basement_works_locations = BasementWorksLocationService()
_roof_works_types = RoofWorksTypeService()
_border_works_types = BorderWorksTypeService()
_access_works_scopes = AccessWorksScopeService()
_access_works_types = AccessWorksTypeService()
_parking_works_scopes = ParkingWorksScopeService()
_equipment_works_types = EquipmentWorksTypeService()
_equipment_works_conservation_types = EquipmentWorksConservationTypeService()
_work_extension_options = WorkExtensionOptionService()

_extension_original_house_single_storey_extensions = \
    ExtensionOriginalHouseSingleStoreyExtensionService()
_extension_original_house_two_storey_extensions = \
    ExtensionOriginalHouseTwoStoreyExtensionService()
_extension_original_house_part_single_part_two_storey_extensions = \
    ExtensionOriginalHousePartSinglePartTwoStoreyExtensionService()
_extension_original_house_basements = ExtensionOriginalHouseBasementService()
_extension_original_house_roof_workss = ExtensionOriginalHouseRoofWorksService()
_extension_original_house_outbuildings = ExtensionOriginalHouseOutbuildingService()
_extension_original_house_porchs = ExtensionOriginalHousePorchService()
_extension_original_house_balcony_terraces = ExtensionOriginalHouseBalconyTerraceService()
_extension_original_house_staircases = ExtensionOriginalHouseStaircaseService()
_extension_original_house_add_replacement_windows_doorss = \
    ExtensionOriginalHouseAddReplacementWindowsDoorsService()
_extension_original_house_claddings = ExtensionOriginalHouseCladdingService()
_works = WorkService()
_work_extension_original_houses = WorkExtensionOriginalHouseService()
_work_extension_incidental_buildingss = WorkExtensionIncidentalBuildingsService()
_work_extension_gates_fences_etcs = WorkExtensionGatesFencesEtcService()
_work_extension_means_of_access_to_sites = WorkExtensionMeansOfAccessToSiteService()
_work_extension_car_bike_spacess = WorkExtensionCarBikeSpacesService()
_work_equipments = WorkEquipmentService()
_work_treess = WorkTreesService()
