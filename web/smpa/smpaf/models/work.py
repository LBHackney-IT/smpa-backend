# -*- coding: utf-8 -*-

"""
    models.work
    ~~~~~~~~~~~
    Works are discrete pieces of work being done as part of a WorksProposal
"""

from .core import BaseModel, ORMMeta
from schematics.types import (  # NOQA
    StringType, BooleanType, DateType, IntType, UUIDType, ListType, FloatType, ModelType
)


class WorksLocation(BaseModel, metaclass=ORMMeta):

    """These can be...

        * ! Rear
        * Side
        * Front
        * Rear / side wrap-around

    TODO: Add these to the statup

    Attributes:
        name (str): The name of the works location
    """

    name = StringType(max_length=255)


####################################################################################################
# Works sub-types
####################################################################################################


class WorkExtensionOption(BaseModel, metaclass=ORMMeta):

    """Base Work Extension sub-work.
    """
    works_location_id = UUIDType()

    @property
    def works_location(self):
        from ..services.work import _works_locations
        return _works_locations.get(self.works_location_id)


class ExtensionOriginalHouseSingleStoreyExtension(WorkExtensionOption):
    pass


class ExtensionOriginalHouseTwoStoreyExtension(WorkExtensionOption):
    pass


class ExtensionOriginalHousePartSinglePartTwoStoreyExtension(WorkExtensionOption):
    pass


class ExtensionOriginalHouseBasement(WorkExtensionOption):
    pass


class ExtensionOriginalHouseRoofWorks(WorkExtensionOption):
    pass


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
    single_storey_extension = ModelType(ExtensionOriginalHouseSingleStoreyExtension)
    two_storey_extension = ModelType(ExtensionOriginalHouseTwoStoreyExtension)
    part_single_part_two_storey_extension = \
        ModelType(ExtensionOriginalHousePartSinglePartTwoStoreyExtension)
    basement = ModelType(ExtensionOriginalHouseBasement)
    roof_works = ModelType(ExtensionOriginalHouseRoofWorks)
    outbuilding = ModelType(ExtensionOriginalHouseOutbuilding)
    porch = ModelType(ExtensionOriginalHousePorch)
    balcony_terrace = ModelType(ExtensionOriginalHouseBalconyTerrace)
    staircase = ModelType(ExtensionOriginalHouseStaircase)
    add_replacement_windows_doors = ModelType(ExtensionOriginalHouseAddReplacementWindowsDoors)
    cladding = ModelType(ExtensionOriginalHouseCladding)


class WorkExtensionIncidentalBuildings(Work):
    pass


class WorkExtensionGatesFencesEtc(Work):
    pass


class WorkExtensionMeansOfAccessToSite(Work):
    pass


class WorkExtensionCarBikeSpaces(Work):
    pass
