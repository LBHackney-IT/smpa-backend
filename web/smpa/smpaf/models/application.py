# -*- coding: utf-8 -*-

"""
    models.application
    ~~~~~~~~~~~~~~~~~~
    Application is our root model. Everything else is part of this.
"""

from .core import BaseModel, ORMMeta
from typing import Type
from datetime import date
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType, ListType,
    FloatType, ModelType, DateType
)

from .user import User


class Application(BaseModel, metaclass=ORMMeta):

    # First screen when starting a new application
    works_started: bool = BooleanType(default=False)
    date_works_started: date = DateType()
    works_completed: bool = BooleanType(default=False)
    date_works_completed: date = DateType()
    works_descreiption: str = StringType()

    owner_id: str = UUIDType()

    #
    # Dynamic relations
    #
    related = {
        'owner_id': '_users',
    }
    owner: Type[User] = ModelType(User)
