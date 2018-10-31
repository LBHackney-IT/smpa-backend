from molten import field, schema
from typing import Optional, Type
from inspect import Parameter
from arrow.arrow import Arrow

from ..helpers.console import console

from .core import (
    BaseResource, BaseManager, BaseComponent, make_base_handler, MetaHandler, handler, Handler
)

from .unit import Area, Linear


@schema
class Dimension(BaseResource):
    proposed_structure_height: Type[Linear]
    proposed_structure_eaves_height: Type[Linear]
    proposed_structure_depth: Type[Linear]
    proposed_structure_width: Type[Linear]
    proposed_building_stories: int
    bedrooms_gained: int
    whole_units_created: int


@schema
class MaterialStructure(BaseResource):

    """Name should be one of:

    Walls
    Roof
    Windows
    Doors
    Lighting
    Access
    """
    name: str


@schema
class MaterialMatch(BaseResource):
    existing_color_and_type: str
    proposed_color_and_type: str


@schema
class Surroundings(BaseResource):

    """TODO:
    string or list of options on:
        * parking_spaces_type
        * type_of_access

    What is?
        * position_of_structure

    """

    distance_from_trees: Type[Linear]
    distance_from_boundary: Type[Linear]
    distance_from_nearest_neighbouring_window: Type[Linear]
    boundry_type: str
    parking_spaces_lost: int
    parking_spaces_gained: int
    parking_spaces_type: str
    creation_of_access: bool
    access_type: str
    position_of_structure: str


@schema
class Development(BaseResource):
    proposed_building_area: Type[Area]
    proposed_building_height: Type[Linear]
    proposed_building_eaves_height: Type[Linear]
    distance_extended_from_original_wall: Type[Linear]
    distance_from_boundary: Type[Linear]
    proposed_building_stories: int
    number_of_bedrooms_gained: int
    existing_materials: str
    proposed_materials: str
    dimensions: Type[Dimension]
    materials_match: Type[MaterialMatch]


@schema
class Proposal(BaseResource):

    """Proposed works top level.
    """

    needs_planning_permission: bool
    description: str
    work_started: bool
    date_started: Type[Arrow]
    work_completed_without_permission: bool
    date_completed: Type[Arrow]
    surroundings: Type[Surroundings]
    development: Type[Development]
