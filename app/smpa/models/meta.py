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
        name (str): The name of the declaration
    """
    name: str = StringType(max_length=255, required=True)


class DeclarationDetail(BaseModel, metaclass=ORMMeta):
    """Free text entry to provide details for a declaration
    """
    name: str = StringType(max_length=255)
    role: str = StringType()
    details: str = StringType()


class OwnershipType(BaseModel, metaclass=ORMMeta):

    """Various types of ownership

    Attributes:
        name (str): The name of the type
    """
    name: str = StringType(max_length=255, required=True)
