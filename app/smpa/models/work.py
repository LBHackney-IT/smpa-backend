# -*- coding: utf-8 -*-

"""
    models.work
    ~~~~~~~~~~~
    Works are discrete pieces of work being done as part of a WorksProposal
"""

from .core import BaseModel, ORMMeta, ListRelType
from schematics.types.serializable import serializable
from schematics.types import (  # NOQA
    StringType, BooleanType, DateType, IntType, UUIDType, ListType, FloatType, ModelType
)


class WorksLocation(BaseModel, metaclass=ORMMeta):

    """These can be...

        * Rear
        * Side
        * Front
        * Rear / side wrap-around

    Attributes:
        name (str): The name of the works location
    """

    name = StringType(max_length=255)


class BasementWorksType(BaseModel, metaclass=ORMMeta):

    """These can be...

        Excavation of a new basement
        Enlargement of an existing basement
        Addition of lightwell(s)
        Other alterations to the appearance of the house

    Attributes:
        name (str): The name of the basement works location
    """

    name = StringType(max_length=255)


class RoofWorksType(BaseModel, metaclass=ORMMeta):

    """Types of work that can be done on a roof.

        Addition of a dormer extension
        Removal of a dormer extension
        Creation of a mansard styled roof extension
        Installation of rooflight(s) and/or roof lantern(s)
        Addition of a new storey(s)
        Alteration of a roof slope
        Replacement of a roof structure and/or covering
        Removal of chimney
        Addition of chimney
    """
    name = StringType(max_length=255)


class BorderWorksType(BaseModel, metaclass=ORMMeta):

    """Types of work that can be done on gates fences and walls.

        Addition of a new entrance
        Removal of an entrance
        Replacement and/or repair of wall
        Replacement and/or repair of pillar caps
    """
    name = StringType(max_length=255)


class AccessWorksScope(BaseModel, metaclass=ORMMeta):

    """Scopes of work that can be done on access to the property

        Only for pedestrian access
        Only for vehicle access
        For vehicle and pedestrian access

    """
    name = StringType(max_length=255)


class AccessWorksType(BaseModel, metaclass=ORMMeta):

    """Types of work that can be done on access to the property

        Addition of a new entrance
        Removal of an entrance
        Improve disabled access
        Dropped kerb and formation of vehicular access
    """
    name = StringType(max_length=255)


class ParkingWorksScope(BaseModel, metaclass=ORMMeta):

    """Scopes of work that can be done on parking

        Only car parking spaces
        Only cycle parking spaces
        Both, car and bike parking spaces

    """
    name = StringType(max_length=255)


class EquipmentWorksType(BaseModel, metaclass=ORMMeta):

    """Types of equipment that can be installed

        Satellite dish or antenna
        Air conditioning unit
        Tank

    """
    name = StringType(max_length=255)


class EquipmentWorksConservationType(BaseModel, metaclass=ORMMeta):

    """Types of equipment that can be installed that need planning permissions
    in a conservation area.

        CCTV
        Security alarm
        Solar panel or other sustainable energy equipment

    """
    name = StringType(max_length=255)


class GatesFencesWallsType(BaseModel, metaclass=ORMMeta):

    """Types of work that can be done on gates, fences and walls.

        Addition of a new gate
        Removal of a gate
        Replacement and/or repair of any boundary treatment
        Replacement and/or repair of pillar caps

    """
    name = StringType(max_length=255)


####################################################################################################
# Works sub-types
####################################################################################################


class WorkExtensionOption(BaseModel, metaclass=ORMMeta):

    """Base Work Extension sub-work.
    """
    works_location_ids = ListRelType(
        UUIDType(),
        to_field='works_locations',
        service='WorksLocationService'
    )
    works_locations = ListType(ModelType(WorksLocation))


class ExtensionOriginalHouseSingleStoreyExtension(WorkExtensionOption):
    pass


class ExtensionOriginalHouseTwoStoreyExtension(WorkExtensionOption):
    pass


class ExtensionOriginalHousePartSinglePartTwoStoreyExtension(WorkExtensionOption):
    pass


class ExtensionOriginalHouseBasement(WorkExtensionOption):
    works_location_ids = ListRelType(
        UUIDType(),
        to_field='works_locations',
        service='WorksLocationService'
    )
    works_locations = ListType(ModelType(WorksLocation))
    works_type_ids = ListRelType(
        UUIDType(),
        to_field='works_types',
        service='BasementWorksTypeService'
    )
    works_types = ListType(ModelType(BasementWorksType))


class ExtensionOriginalHouseRoof(WorkExtensionOption):
    works_type_ids = ListRelType(
        UUIDType(),
        to_field='works_types',
        service='RoofWorksTypeService'
    )
    works_types = ListType(ModelType(RoofWorksType))


class ExtensionOutbuilding(WorkExtensionOption):
    pass


class ExtensionOriginalHousePorch(WorkExtensionOption):
    pass


class ExtensionOriginalHouseBalconyTerrace(WorkExtensionOption):
    pass


class ExtensionOriginalHouseStaircase(WorkExtensionOption):
    pass


class ExtensionOriginalHouseWindowsDoors(WorkExtensionOption):
    pass


class ExtensionOriginalHouseCladding(WorkExtensionOption):
    pass


class ExtensionBoundaraiesGatesFencesWalls(WorkExtensionOption):
    works_location_ids = ListRelType(
        UUIDType(),
        to_field='works_locations',
        service='WorksLocationService'
    )
    works_locations = ListType(ModelType(WorksLocation))
    works_type_ids = ListRelType(
        UUIDType(),
        to_field='works_types',
        service='GatesFencesWallsTypeService'
    )
    works_types = ListType(ModelType(GatesFencesWallsType))


####################################################################################################
# Works Types
####################################################################################################


class Work(BaseModel, metaclass=ORMMeta):

    """The base work.
    """
    pass


# ExtensionProposal Works


class WorkExtensionOriginalHouse(Work):

    """Summary
    """
    single_storey_extension = ModelType(ExtensionOriginalHouseSingleStoreyExtension)
    two_storey_extension = ModelType(ExtensionOriginalHouseTwoStoreyExtension)
    part_single_part_two_storey_extension = \
        ModelType(ExtensionOriginalHousePartSinglePartTwoStoreyExtension)
    basement = ModelType(ExtensionOriginalHouseBasement)
    roof = ModelType(ExtensionOriginalHouseRoof)
    porch = ModelType(ExtensionOriginalHousePorch)
    balcony_terrace = ModelType(ExtensionOriginalHouseBalconyTerrace)
    staircase = ModelType(ExtensionOriginalHouseStaircase)
    windows_doors = ModelType(ExtensionOriginalHouseWindowsDoors)
    cladding = ModelType(ExtensionOriginalHouseCladding)


class WorkExtensionIncidentalBuildings(Work):
    removal_or_demolition = BooleanType(default=False)
    details = StringType()
    outbuilding = ModelType(ExtensionOutbuilding)


class WorkExtensionBoundaries(Work):
    gates_fences_walls = ModelType(ExtensionBoundaraiesGatesFencesWalls)
    # TODO Probably removing
    border_works_type_ids = ListRelType(
        UUIDType(),
        to_field='border_works_types',
        service='BorderWorksTypeService'
    )
    border_works_types = ListType(ModelType(BorderWorksType))


class WorkExtensionMeansOfAccess(Work):
    access_works_scope_id = UUIDType()
    access_works_scope = ModelType(BorderWorksType)

    access_works_sub_type_ids = ListRelType(
        UUIDType(),
        to_field='access_works_sub_types',
        service='AccessWorksTypeService'
    )
    access_works_sub_types = ListType(ModelType(AccessWorksType))


class WorkExtensionParking(Work):
    parking_works_scope_id = UUIDType()
    parking_works_scope = ModelType(ParkingWorksScope)

    # This looks unused?
    # parking_works_sub_type_ids = ListRelType(
    #     UUIDType(),
    #     to_field='parking_works_sub_types',
    #     service='ParkingWorksSubTypeService'
    # )
    # parking_works_sub_types = ListType(ModelType(ParkingWorksSubType))

    current_car_parking_spaces = IntType(default=0)
    planned_car_parking_spaces = IntType(default=0)
    current_bike_parking_spaces = IntType(default=0)
    planned_bike_parking_spaces = IntType(default=0)
    new_ev_charging_points = IntType(default=0)


####################################################################################################
# Equipment works
####################################################################################################


class WorkEquipmentLocation(BaseModel, metaclass=ORMMeta):

    location_ids = ListRelType(
        UUIDType(),
        to_field='locations',
        service='WorksLocationService'
    )
    locations = ListType(ModelType(WorksLocation))

    equipment_type_id = UUIDType()
    equipment_type = ModelType(EquipmentWorksType)


class WorkEquipmentConservationLocation(BaseModel, metaclass=ORMMeta):

    location_id = UUIDType()
    location = ModelType(WorksLocation)

    equipment_type_id = UUIDType()
    equipment_conservation_type = ModelType(EquipmentWorksConservationType)


class WorkEquipment(BaseModel, metaclass=ORMMeta):

    equipment_type_ids = ListRelType(
        UUIDType(),
        to_field='equipment_types',
        service='EquipmentWorksTypeService'
    )
    equipment_types = ListType(ModelType(EquipmentWorksType))

    equipment_conservation_type_ids = ListRelType(
        UUIDType(),
        to_field='equipment_conservation_types',
        service='EquipmentWorksConservationTypeService'
    )
    equipment_conservation_types = ListType(ModelType(EquipmentWorksConservationType))

    equipment_locations = ListType(ModelType(WorkEquipmentLocation))
    equipment_conservation_locations = ListType(ModelType(WorkEquipmentLocation))


####################################################################################################
# Tree works
####################################################################################################


class WorkTrees(BaseModel, metaclass=ORMMeta):
    inside_boundry = BooleanType(default=False)
    removed_or_pruned = BooleanType(default=False)
    outside_boundry = BooleanType(default=False)
