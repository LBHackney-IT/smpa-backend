# -*- coding: utf-8 -*-

"""
    models.tmp
    ~~~~~~~~~~
    Temp testing models
"""

from .core import MongoModel, BaseModel, ORMMeta, RelType
from schematics.types.serializable import serializable
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType, ListType, FloatType, ModelType
)


####################################################################################################
# Material options are the predefined lists of materials
####################################################################################################


class TempModel(MongoModel, metaclass=ORMMeta):

    """A pre-defined list of materials
    """
    name = StringType(max_length=100, required=True)
    something = StringType(max_length=255)
