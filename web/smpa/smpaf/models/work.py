# -*- coding: utf-8 -*-

"""
    models.work
    ~~~~~~~~~~~
    Works are discrete pieces of work being done as part of a WorksProposal
"""

from .core import BaseModel, ORMMeta
from schematics.types.serializable import serializable
from schematics.types import (  # NOQA
    StringType, BooleanType, DateType, IntType, UUIDType, ListType, FloatType, ModelType
)

from marshmallow import fields, validate, pprint  # NOQA


class WorksLocation(BaseModel, metaclass=ORMMeta):

    """These can be...

        * Rear
        * Side
        * Front
        * Rear / side wrap-around

    Attributes:
        name (str): The name of the works location
    """

    name = fields.Str(validate=validate.Length(max=255), required=True)


class BasementWorksLocation(BaseModel, metaclass=ORMMeta):

    """These can be...

        Excavation of a new basement
        Enlargement of an existing basement
        Addition of lightwell(s)
        Other alterations to the appearance of the house

    Attributes:
        name (str): The name of the basement works location
    """

    name = fields.Str(validate=validate.Length(max=255), required=True)


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

    TODO: add these to startup
    """
    name = fields.Str(validate=validate.Length(max=255), required=True)


class BorderWorksType(BaseModel, metaclass=ORMMeta):

    """Types of work that can be done on gates fences and walls.

        Addition of a new entrance
        Removal of an entrance
        Replacement and/or repair of wall
        Replacement and/or repair of pillar caps

    TODO: add these to startup
    """
    name = fields.Str(validate=validate.Length(max=255), required=True)


class AccessWorksScope(BaseModel, metaclass=ORMMeta):

    """Scopes of work that can be done on access to the property

        Only for pedestrian access
        Only for vehicle access
        For vehicle and pedestrian access

    TODO: add these to startup
    """
    name = fields.Str(validate=validate.Length(max=255), required=True)


class AccessWorksType(BaseModel, metaclass=ORMMeta):

    """Types of work that can be done on access to the property

        Addition of a new entrance
        Removal of an entrance
        Improve disabled access
        Dropped kerb and formation of vehicular access

    TODO: add these to startup
    """
    name = fields.Str(validate=validate.Length(max=255), required=True)


class ParkingWorksScope(BaseModel, metaclass=ORMMeta):

    """Scopes of work that can be done on parking

        Only car parking spaces
        Only cycle parking spaces
        Both, car and bike parking spaces

    TODO: add these to startup
    """
    name = fields.Str(validate=validate.Length(max=255), required=True)


class EquipmentWorksType(BaseModel, metaclass=ORMMeta):

    """Types of equipment that can be installed

        Satellite dish or antenna
        Air conditioning unit
        Tank

    TODO: add these to startup
    """
    name = fields.Str(validate=validate.Length(max=255), required=True)


class EquipmentWorksConservationType(BaseModel, metaclass=ORMMeta):

    """Types of equipment that can be installed that need planning permissions
    in a conservation area.

        CCTV
        Security alarm
        Solar panel or other sustainable energy equipment

    TODO: add these to startup
    """
    name = fields.Str(validate=validate.Length(max=255), required=True)


####################################################################################################
# Works sub-types
####################################################################################################


class WorkExtensionOption(BaseModel, metaclass=ORMMeta):

    """Base Work Extension sub-work.
    """
    works_location_ids = fields.List(fields.UUID())

    @serializable
    def works_locations(self):
        from ..services.work import _works_locations
        return [_works_locations.get(_).to_native() for _ in self.works_location_ids]


class ExtensionOriginalHouseSingleStoreyExtension(WorkExtensionOption):
    pass


class ExtensionOriginalHouseTwoStoreyExtension(WorkExtensionOption):
    pass


class ExtensionOriginalHousePartSinglePartTwoStoreyExtension(WorkExtensionOption):
    pass


class ExtensionOriginalHouseBasement(WorkExtensionOption):
    basement_works_location_ids = fields.List(fields.UUID())

    @serializable
    def basement_works_locations(self):
        from ..services.work import _basement_works_locations
        return [_basement_works_locations.get(_).to_native()
                for _ in self.basement_works_location_ids]


class ExtensionOriginalHouseRoofWorks(WorkExtensionOption):
    roof_works_type_ids = fields.List(fields.UUID())

    @serializable
    def works_types(self):
        from ..services.work import _roof_works_types
        return [_roof_works_types.get(_).to_native() for _ in self.roof_works_type_ids]


class ExtensionOriginalHouseOutbuilding(WorkExtensionOption):
    pass


class ExtensionOriginalHousePorch(WorkExtensionOption):
    pass


class ExtensionOriginalHouseBalconyTerrace(WorkExtensionOption):
    pass


class ExtensionOriginalHouseStaircase(WorkExtensionOption):
    pass


class ExtensionOriginalHouseAddReplacementWindowsDoors(WorkExtensionOption):
    pass


class ExtensionOriginalHouseCladding(WorkExtensionOption):
    pass


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
    single_storey_extension = fields.Nested(ExtensionOriginalHouseSingleStoreyExtension)
    two_storey_extension = fields.Nested(ExtensionOriginalHouseTwoStoreyExtension)
    part_single_part_two_storey_extension = \
        fields.Nested(ExtensionOriginalHousePartSinglePartTwoStoreyExtension)
    basement = fields.Nested(ExtensionOriginalHouseBasement)
    roof_works = fields.Nested(ExtensionOriginalHouseRoofWorks)
    outbuilding = fields.Nested(ExtensionOriginalHouseOutbuilding)
    porch = fields.Nested(ExtensionOriginalHousePorch)
    balcony_terrace = fields.Nested(ExtensionOriginalHouseBalconyTerrace)
    staircase = fields.Nested(ExtensionOriginalHouseStaircase)
    add_replacement_windows_doors = fields.Nested(ExtensionOriginalHouseAddReplacementWindowsDoors)
    cladding = fields.Nested(ExtensionOriginalHouseCladding)


class WorkExtensionIncidentalBuildings(Work):
    removal_or_demolition = fields.Boolean(default=False)
    details = fields.Str()


class WorkExtensionGatesFencesEtc(Work):
    border_works_type_ids = fields.List(fields.UUID())

    @serializable
    def works_types(self):
        from ..services.work import _border_works_types
        return [_border_works_types.get(_).to_native() for _ in self.border_works_type_ids]


class WorkExtensionMeansOfAccessToSite(Work):
    access_works_scope_id = fields.UUID()
    access_works_sub_type_ids = fields.List(fields.UUID())

    @serializable
    def works_scope(self):
        from ..services.work import _access_works_scopes
        return _access_works_scopes.get(self.access_works_scope_id).to_native()

    @serializable
    def works_sub_types(self):
        from ..services.work import _access_works_sub_types
        return [_access_works_sub_types.get(_).to_native() for _ in self.access_works_sub_type_ids]


class WorkExtensionCarBikeSpaces(Work):
    parking_works_scope_id = fields.UUID()
    parking_works_sub_type_ids = fields.List(fields.UUID())
    current_car_parking_spaces = fields.Integer(default=0)
    planned_car_parking_spaces = fields.Integer(default=0)
    current_bike_parking_spaces = fields.Integer(default=0)
    planned_bike_parking_spaces = fields.Integer(default=0)
    new_ev_charging_points = fields.Integer(default=0)

    @serializable
    def works_scope(self):
        from ..services.work import _parking_works_scopes
        return _parking_works_scopes.get(self.parking_works_scope_id).to_native()


####################################################################################################
# Equipment works
####################################################################################################


class WorkEquipment(BaseModel, metaclass=ORMMeta):
    equipment_type_ids = fields.List(fields.UUID())
    equipment_conservation_type_ids = fields.List(fields.UUID())

    @serializable
    def equipment_types(self):
        from ..services.work import _equipment_types
        return [_equipment_types.get(_).to_native() for _ in self.equipment_type_ids]

    @serializable
    def equipment_conservation_types(self):
        from ..services.work import _equipment_conservation_types
        return [_equipment_conservation_types.get(_).to_native()
                for _ in self.equipment_conservation_type_ids]


####################################################################################################
# Tree works
####################################################################################################


class WorkTrees(BaseModel, metaclass=ORMMeta):
    inside_boundry = fields.Boolean(default=False)
    removed_or_pruned = fields.Boolean(default=False)
    outside_boundry = fields.Boolean(default=False)
