# -*- coding: utf-8 -*-

"""
    models.test
    ~~~~~~~~~~~
    test model
"""
from .core import BaseModel, ORMMeta
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType
)


class Test(BaseModel, metaclass=ORMMeta):

    """This is a test model, for testing things with.
    """

    name = StringType(required=True)

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.name}>'
