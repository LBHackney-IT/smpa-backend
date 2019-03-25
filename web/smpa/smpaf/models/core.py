# -*- coding: utf-8 -*-

"""
    smpa.models.core
    ~~~~~~~~~~~~~~~~
    BaseModel class
"""

import datetime
from inflection import tableize
# from schematics.models import Model, ModelMeta
# from schematics.exceptions import ValidationError
# from schematics.types import (
#     StringType, BooleanType, DateTimeType, IntType, UUIDType
# )

from marshmallow.schema import SchemaMeta
from marshmallow.validate import ValidationError
from marshmallow import Schema, fields, validate, pprint  # NOQA

from ..rdb.registry import model_registry
from ..helpers.console import console


class ORMMeta(SchemaMeta):

    instance = None

    def __new__(cls, name, bases, dct):
        # console.info('ORMMeta {}'.format(name))
        if name != "BaseModel":
            # We have a model class
            cls._table = tableize(name)
            super_new = super().__new__
            new_class = super_new(cls, name, bases, dct)
            cls._model = new_class
            setattr(new_class, '_table', cls._table)
            # register the model
            model_registry.add(name, new_class, cls)

        return new_class


class BaseModel(Schema):

    _uniques = []

    id = fields.UUID()
    created_at: datetime = fields.DateTime(default=datetime.datetime.now)
    updated_at: datetime = fields.DateTime(default=datetime.datetime.now)

    def __repr__(self):
        if hasattr(self, 'email'):
            return u'<{}: {}>'.format(self.__class__.__name__, self.email)
        if hasattr(self, 'slug'):
            return u'<{}: {}>'.format(self.__class__.__name__, self.slug)
        if hasattr(self, 'name'):
            return u'<{}: {}>'.format(self.__class__.__name__, self.name)
        if hasattr(self, 'id'):
            return u'<{}: {}>'.format(self.__class__.__name__, self.id)
        return u'<{}: {} object>'.format(self.__class__.__name__, self.__class__.__name__)


class CoreGetSchema(Schema):
    id = fields.UUID()
