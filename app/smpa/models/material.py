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
    # matches_existing = BooleanType(default=False)
    # existing_material = ModelType(BaseExistingMaterial)


####################################################################################################
# Answers to "Other"
####################################################################################################


class MaterialRoof(BaseMaterial):
    material_id = UUIDType()


class MaterialWall(BaseMaterial):
    material_id = UUIDType()


class MaterialWindow(BaseMaterial):
    material_id = UUIDType()


class MaterialDoor(BaseMaterial):
    material_id = UUIDType()


class OtherMaterial(BaseMaterial):
    name = StringType(required=True)


class ExternalBuildingMaterial(BaseModel, metaclass=ORMMeta):
    element = StringType(required=True)
    proposed_material = StringType(required=True)
    colour_and_type = StringType(required=True)


class MaterialProposalRoof(BaseModel, metaclass=ORMMeta):
    proposals = ListType(ModelType(MaterialRoof))
    matches_existing = BooleanType(default=False)
    not_applicable = BooleanType(default=False)


class MaterialProposalWalls(BaseModel, metaclass=ORMMeta):
    proposals = ListType(ModelType(MaterialRoof))
    matches_existing = BooleanType(default=False)
    not_applicable = BooleanType(default=False)


class MaterialProposalWindows(BaseModel, metaclass=ORMMeta):
    proposals = ListType(ModelType(MaterialRoof))
    matches_existing = BooleanType(default=False)
    not_applicable = BooleanType(default=False)


class MaterialProposalDoors(BaseModel, metaclass=ORMMeta):
    proposals = ListType(ModelType(MaterialRoof))
    matches_existing = BooleanType(default=False)
    not_applicable = BooleanType(default=False)


####################################################################################################
# MaterialProposal is the materials key in models.proposal.ExtensionProposal
####################################################################################################

class MaterialExtension(BaseModel, metaclass=ORMMeta):
    # You will define materials on supporting documentation
    definitions_in_documents = BooleanType(default=False)
    # You will define materials using this form <- we can ignore
    definitions_in_form = BooleanType(default=False)
    # You don’t know yet and will submit an Approval of Conditions later
    definitions_to_follow = BooleanType(default=False)

    roof = ModelType(MaterialProposalRoof)
    walls = ModelType(MaterialProposalWalls)
    windows = ModelType(MaterialProposalWindows)
    doors = ModelType(MaterialProposalDoors)
