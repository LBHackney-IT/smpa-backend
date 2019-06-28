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
    works_location_ids = ListType(UUIDType())
    works_locations = ListType(ModelType(WorksLocation))
    works_type_ids = ListType(UUIDType())
    works_types = ListType(ModelType(BasementWorksType))

    related_lists = [
        ('works_location_ids', 'works_locations', 'WorksLocationService'),
        ('works_type_ids', 'works_types', 'BasementWorksTypeService'),
    ]


class ExtensionOriginalHouseRoof(WorkExtensionOption):
    works_type_ids = ListType(UUIDType())
    works_types = ListType(ModelType(RoofWorksType))

    materials_ids = ListType(UUIDType())
    materials = ListType(ModelType('smpa.models.material.MaterialOptionRoof'))

    materials_not_applicable = BooleanType(default=False)
    materials_match_existing = BooleanType(default=False)

    related_lists = [
        ('works_type_ids', 'works_types', 'RoofWorksTypeService'),
    ]


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
    works_location_ids = ListType(UUIDType())
    works_locations = ListType(ModelType(WorksLocation))
    works_type_ids = ListType(UUIDType())
    works_types = ListType(ModelType(GatesFencesWallsType))

    related_lists = [
        ('works_location_ids', 'works_locations', 'WorksLocationService'),
        ('works_type_ids', 'works_types', 'GatesFencesWallsTypeService'),
    ]


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
    border_works_type_ids = ListType(UUIDType())
    border_works_types = ListType(ModelType(BorderWorksType))


class WorkExtensionMeansOfAccess(Work):
    access_works_scope_id = UUIDType()
    access_works_scope = ModelType(BorderWorksType)

    access_works_sub_type_ids = ListType(UUIDType())
    access_works_sub_types = ListType(ModelType(AccessWorksType))


class WorkExtensionParking(Work):
    parking_works_scope_id = UUIDType()
    parking_works_scope = ModelType(ParkingWorksScope)

    parking_works_sub_type_ids = ListType(UUIDType())
    # parking_works_sub_types = ListType(ModelType())

    current_car_parking_spaces = IntType(default=0)
    planned_car_parking_spaces = IntType(default=0)
    current_bike_parking_spaces = IntType(default=0)
    planned_bike_parking_spaces = IntType(default=0)
    new_ev_charging_points = IntType(default=0)


####################################################################################################
# Equipment works
####################################################################################################


class WorkEquipmentLocation(BaseModel, metaclass=ORMMeta):

    location_ids = ListType(UUIDType())
    locations = ListType(ModelType(WorksLocation))

    equipment_type_id = UUIDType()
    equipment_type = ModelType(EquipmentWorksType)

    # TODO Add relationships


class WorkEquipmentConservationLocation(BaseModel, metaclass=ORMMeta):

    location_id = UUIDType()
    location = ModelType(WorksLocation)

    equipment_type_id = UUIDType()
    equipment_conservation_type = ModelType(EquipmentWorksConservationType)

    # TODO Add relationships


class WorkEquipment(BaseModel, metaclass=ORMMeta):

    equipment_type_ids = ListType(UUIDType())
    equipment_types = ListType(ModelType(EquipmentWorksType))

    equipment_conservation_type_ids = ListType(UUIDType())
    equipment_conservation_types = ListType(ModelType(EquipmentWorksConservationType))

    equipment_locations = ListType(ModelType(WorkEquipmentLocation))
    equipment_conservation_locations = ListType(ModelType(WorkEquipmentLocation))

    # TODO Add relationships


####################################################################################################
# Tree works
####################################################################################################


class WorkTrees(BaseModel, metaclass=ORMMeta):
    inside_boundry = BooleanType(default=False)
    removed_or_pruned = BooleanType(default=False)
    outside_boundry = BooleanType(default=False)
