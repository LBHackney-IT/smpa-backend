# -*- coding: utf-8 -*-

"""
    models.site
    ~~~~~~~~~~~
    Planning site related models.
"""

from .core import BaseModel, ORMMeta
from schematics.types.serializable import serializable
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType, ListType, FloatType, ModelType
)

####################################################################################################
# Material options are the predefined lists of materials
####################################################################################################


class MaterialOption(BaseModel, metaclass=ORMMeta):

    """A pre-defined list of materials
    """
    name = StringType(max_length=100, required=True)


class MaterialOptionRoof(MaterialOption):

    """Options for roof materials

        Tiles
        Concrete
        Slate
        Metal
        Thatch
        Asphalt shingles
        Unknown

    """

    pass


class MaterialOptionWall(MaterialOption):
    pass


class MaterialOptionWindow(MaterialOption):
    pass


class MaterialOptionDoor(MaterialOption):
    pass


####################################################################################################
# Base materials entered by users
####################################################################################################


class BaseExistingMaterial(BaseModel, metaclass=ORMMeta):
    name = StringType(required=True)
    colour_and_type = StringType(required=True)


class BaseMaterial(BaseModel, metaclass=ORMMeta):
    colour_and_type = StringType(required=True)
    matches_existing = BooleanType(default=False)
    existing_material = ModelType(BaseExistingMaterial)


####################################################################################################
# Answers to "Other"
####################################################################################################


class MaterialRoofOther(BaseMaterial):
    material_id = UUIDType()


class MaterialWallOther(BaseMaterial):
    material_id = UUIDType()


class MaterialWindowOther(BaseMaterial):
    material_id = UUIDType()


class MaterialDoorOther(BaseMaterial):
    material_id = UUIDType()


class OtherMaterialOther(BaseMaterial):
    name = StringType(required=True)


class ExternalBuildingMaterial(BaseModel, metaclass=ORMMeta):
    element = StringType(required=True)
    proposed_material = StringType(required=True)
    colour_and_type = StringType(required=True)
