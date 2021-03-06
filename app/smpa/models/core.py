# -*- coding: utf-8 -*-

"""
    smpa.models.core
    ~~~~~~~~~~~~~~~~
    BaseModel class
"""

import json
import arrow
import datetime
from importlib import import_module
from schematics.models import Model, ModelMeta
from schematics.transforms import blacklist
from inflection import tableize, underscore
from bson.objectid import ObjectId
from schematics.contrib.mongo import ObjectIdType
from schematics.types import (
    StringType, BooleanType, DateTimeType, IntType, UUIDType, BaseType, ListType
)

from schematics.exceptions import ValidationError
from schematics.transforms import Converter, PRIMITIVE

# from ..rdb.registry import model_registry
from smpa.db.documentdb.registry import model_registry
from smpa.helpers.console import console


class JSONBlobType(BaseType):
    """Because sometimes we need to save a blob of json for which we have no idea
    what the format will be.
    """
    def to_native(self, value, context=None):
        return json.loads(json.dumps(value))

    def to_primitive(self, value, context=None):
        return json.dumps(value)


class ListRelType(BaseType):

    """Provide a mechanism for getting related lists of objects.
    """
    def __init__(self, field, to_field, service, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self._to_field = to_field
        self._service = service

    @property
    def default(self):
        return []


class RelType(BaseType):

    """Provide a mechanism for getting an fk related object.
    """
    def __init__(self, field, to_field, service, *args, **kwargs):
        req = kwargs.pop('required', False)
        super().__init__(self, field, *args, **kwargs)
        self._to_field = to_field
        self._service = service
        self.required = req

    @property
    def default(self):
        return None


class ArrowDTType(BaseType):

    primitive_type = str
    native_type = datetime.datetime

    def to_native(self, value, context=None):
        return arrow.get(value).datetime

    def to_primitive(self, value, context=None):
        return arrow.get(value).isoformat()


class RelConverter(Converter):

    def __call__(self, field, value, context):
        format = PRIMITIVE
        # console.log(type(field))
        if type(field) == ListRelType:
            return self._convert_list(field, value, context)
        if type(field) == RelType:
            return self._convert_fk(field, value, context)

        return field.export(value, format, context)

    def _convert_fk(self, field, value, context):
        try:
            service = self._get_service_instance(field)
            setattr(field.owner_model, field._to_field, service.get(value))
        except Exception as e:
            console.warn(e)

        return value

    def _convert_list(self, field, value, context):
        service = self._get_service_instance(field)
        results = []
        ids = value
        for id in ids:
            results.append(service.get(id))

        setattr(field.owner_model, field._to_field, results)
        return value

    def _get_service_instance(self, field):
        module = import_module('smpa.services')
        service_class = getattr(module, field._service)
        if callable(service_class):
            service = service_class()
        else:
            service = service_class

        return service

    def pre(self, model_class, instance_or_dict, context):
        return instance_or_dict

    def post(self, model_class, data, context):
        return data


rel_exporter = RelConverter()


class ORMMeta(ModelMeta):

    instance = None

    def __new__(cls, name, bases, dct):
        # console.info('ORMMeta {}'.format(name))
        if name != "BaseModel":
            # We have a model class
            cls._table = tableize(name)[:56]
            super_new = super(ORMMeta, cls).__new__
            new_class = super_new(cls, name, bases, dct)
            cls._model = new_class
            setattr(new_class, '_table', cls._table)
            # register the model
            model_registry.add(name, new_class, cls)

        return new_class


class RDBModel(Model):

    _uniques: list = []
    _uniques_not_none: list = []

    id: str = UUIDType()
    created_at: datetime.datetime = DateTimeType()
    updated_at: datetime.datetime = DateTimeType()

    def validate(self):
        # console.debug('VALIDATING')
        for field in self._uniques:
            # console.debug('Validate that {} is unique'.format(field))
            value = self._data.get(field, None)
            if value is not None:
                query = {field: value}
                _ = self._service.first(**query)
                if _ is not None and str(_.id) != str(self.id):
                    raise ValidationError(
                        'Field `{}` must be unique, found value {}'.format(field, value))

        for field in self._uniques_not_none:
            value = self._data.get(field, None)
            if value is None:
                raise ValidationError('Unique fields cannot be None ({})'.format(field))

        return super().validate()

    def export(self):
        if hasattr(self, 'backrefs'):
            self._get_backrefs()
        if hasattr(self, 'list_backrefs'):
            self._get_list_backrefs()
        return super().export(field_converter=rel_exporter)

    def to_primitive(self):
        if hasattr(self, 'backrefs'):
            self._get_backrefs()
        if hasattr(self, 'list_backrefs'):
            self._get_list_backrefs()
        return super().to_primitive()

    #
    # Private methods for serializing relationships
    #

    def _get_service_instance(self, service_name):
        module = import_module('smpa.services')
        service_class = getattr(module, service_name)
        if callable(service_class):
            service = service_class()
        else:
            service = service_class

        return service

    def _get_backrefs(self):
        if hasattr(self, 'backrefs'):
            for d in self.backrefs:
                field, service_name = d[0], d[1]
                try:
                    service = self._get_service_instance(service_name)
                    query = {field: str(self.id)}
                    related = service.first(**query)
                    prop = underscore(service.__model__.__name__)
                    # console.log(f'Setting {prop} on {self} to {related}')
                    setattr(self, prop, related)
                except Exception as e:
                    console.warn(e)

    def _get_list_backrefs(self):
        if hasattr(self, 'list_backrefs'):
            for d in self.list_backrefs:
                field, service_name, prop = d[0], d[1], d[2]
                try:
                    service = self._get_service_instance(service_name)
                    query = {field: str(self.id)}
                    related = service.find(**query)
                    setattr(self, prop, related)
                except Exception as e:
                    console.warn(e)

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


class MongoModel(RDBModel):

    class Options:
        roles = {
            'default': blacklist('_id', )
        }

    _id: ObjectId = ObjectIdType()


class BaseModel(MongoModel):
    pass
