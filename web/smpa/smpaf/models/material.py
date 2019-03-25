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

from marshmallow import fields, validate, pprint  # NOQA

####################################################################################################
# Material options are the predefined lists of materials
####################################################################################################


class MaterialOption(BaseModel, metaclass=ORMMeta):

    """A pre-defined list of materials
    """
    name: str = fields.Str(validate=validate.Length(max=100), required=True)


class MaterialOptionRoof(MaterialOption):
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
    matches_existing = fields.Boolean(default=False)
    existing_material = fields.Nested(BaseExistingMaterial)


####################################################################################################
# comment
####################################################################################################


class MaterialRoof(BaseMaterial):
    material_id = fields.UUID()

    @serializable
    def material(self):
        from ..services.material import _material_options_roof
        return _material_options_roof.get(self.material_id).to_native()


class MaterialWall(BaseMaterial):
    material_id = fields.UUID()

    @serializable
    def material(self):
        from ..services.material import _material_options_wall
        return _material_options_wall.get(self.material_id).to_native()


class MaterialWindow(BaseMaterial):
    material_id = fields.UUID()

    @serializable
    def material(self):
        from ..services.material import _material_options_window
        return _material_options_window.get(self.material_id).to_native()


class MaterialDoor(BaseMaterial):
    material_id = fields.UUID()

    @serializable
    def material(self):
        from ..services.material import _material_options_door
        return _material_options_door.get(self.material_id).to_native()


class OtherMaterial(BaseMaterial):
    name = StringType(required=True)


class ExternalBuildingMaterial(BaseModel, metaclass=ORMMeta):
    element = StringType(required=True)
    proposed_material = StringType(required=True)
    colour_and_type = StringType(required=True)
