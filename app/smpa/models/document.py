# -*- coding: utf-8 -*-

"""
    models.document
    ~~~~~~~~~~~~~~~
    Document related models.
"""
from typing import Type

from .core import BaseModel, ORMMeta, RelType
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType, ListType, FloatType, ModelType
)


class DocumentSize(BaseModel, metaclass=ORMMeta):

    """For storing document sizes. Although why anyone would need to do this
    in 2019 remains to be seen.

    Attributes:
        name (Unicode): The size, ie: A4, A3 etc.
    """
    name = StringType(max_length=20, required=True)


class DocumentFile(BaseModel, metaclass=ORMMeta):
    original_name = StringType(required=True)
    storage_path = StringType(required=True)
    # Relationships
    application_id: str = UUIDType()
    document_size_id = RelType(
        UUIDType(),
        to_field='document_size',
        service='DocumentSizeService'
    )
    document_size: Type[DocumentSize] = ModelType(DocumentSize)
