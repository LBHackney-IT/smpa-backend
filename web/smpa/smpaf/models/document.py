# -*- coding: utf-8 -*-

"""
    models.document
    ~~~~~~~~~~~~~~~
    Document related models.
"""

from .core import BaseModel, ORMMeta
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType, ListType, FloatType
)


class DocumentSize(BaseModel, metaclass=ORMMeta):

    """For storing document sizes. Although why anyone would need to do this
    in 2019 remains to be seen.

    Attributes:
        name (Unicode): The size, ie: A4, A3 etc.
    """
    name = StringType(max_length=20, required=True)
