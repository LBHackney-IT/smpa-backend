# -*- coding: utf-8 -*-

"""
    models.meta
    ~~~~~~~~~~~
    Meta models.
"""

from .core import BaseModel, ORMMeta
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType
)


class Declaration(BaseModel, metaclass=ORMMeta):

    """Various declarations of a conflict of interest

    Attributes:
        name (TYPE): The name of the declaration
    """
    name: str = StringType(max_length=255, required=True)
