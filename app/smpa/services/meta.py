# -*- coding: utf-8 -*-

"""
    services.meta
    ~~~~~~~~~~~~~
    Services for meta models.
"""

from .mongo import DService

from ..models.meta import Declaration, OwnershipType


class DeclarationService(DService):
    __model__ = Declaration


_declarations = DeclarationService()


class OwnershipTypeService(DService):
    __model__ = OwnershipType


_ownership_types = OwnershipTypeService()
