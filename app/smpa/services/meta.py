# -*- coding: utf-8 -*-

"""
    services.meta
    ~~~~~~~~~~~~~
    Services for meta models.
"""

from .mongo import DService

from ..models.meta import Declaration


class DeclarationService(DService):
    __model__ = Declaration


_declarations = DeclarationService()
