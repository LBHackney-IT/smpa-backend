# -*- coding: utf-8 -*-

"""
    models.application
    ~~~~~~~~~~~~~~~~~~
    Application is our root model. Everything else is part of this.
"""

from .core import BaseModel, ORMMeta
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType, ListType,
    FloatType, ModelType, DateType
)

from marshmallow import fields, validate, pprint  # NOQA


class Application(BaseModel, metaclass=ORMMeta):

    # First screen when starting a new application
    works_started = fields.Boolean(default=False)
    date_works_started = fields.Date()
    works_completed = fields.Boolean(default=False)
    date_works_completed = fields.Date()
    works_descreiption = fields.Str()
