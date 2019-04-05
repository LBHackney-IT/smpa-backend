# -*- coding: utf-8 -*-

"""
    services.unit
    ~~~~~~~~~~~~~
    Services for units of measurement.
"""

from .rethink import RService

from ..models.document import DocumentSize


class DocumentSizeService(RService):
    __model__ = DocumentSize


_document_sizes = DocumentSizeService()
