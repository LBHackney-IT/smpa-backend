# -*- coding: utf-8 -*-

"""
    smpa.models.core
    ~~~~~~~~~~~~~~~~
    BaseModel class
"""

import datetime
from importlib import import_module
from schematics.models import Model, ModelMeta
from inflection import tableize, underscore
from schematics.types import (
    StringType, BooleanType, DateTimeType, IntType, UUIDType, BaseType
)

from schematics.exceptions import ValidationError

from ..rdb.registry import model_registry
from ..helpers.console import console


class ORMMeta(ModelMeta):

    instance = None

    def __new__(cls, name, bases, dct):
        # console.info('ORMMeta {}'.format(name))
        if name != "BaseModel":
            # We have a model class
            cls._table = tableize(name)
            super_new = super(ORMMeta, cls).__new__
            new_class = super_new(cls, name, bases, dct)
            cls._model = new_class
            setattr(new_class, '_table', cls._table)
            # register the model
            model_registry.add(name, new_class, cls)

        return new_class


class BaseModel(Model):

    _uniques = []

    id: str = UUIDType()
    created_at: datetime = DateTimeType(default=datetime.datetime.now)
    updated_at: datetime = DateTimeType(default=datetime.datetime.now)

    def validate(self):
        console.debug('VALIDATING')
        for field in self._uniques:
            console.debug('Validate that {} is unique'.format(field))
            if self._data.get(field, None) is None:
                raise ValidationError('Unique fields cannot be None ({})'.format(field))
            _ = self.query.get_by(column=field, value=self._data.get(field, None))
            if _ is not None and _.id != self.id:
                raise ValidationError('Field `{}` must be unique'.format(field))
        return super(BaseModel, self).validate()

    def to_primitive(self):
        if hasattr(self, 'related_lists'):
            self._get_related_lists()
        if hasattr(self, 'related'):
            self._get_related()
        if hasattr(self, 'backrefs'):
            self._get_backrefs()

        return super().to_primitive()

    #
    # Private methods for serializing relationships

    def _get_related_lists(self):
        import ipdb; ipdb.set_trace()
        for d in self.related_lists:
            field, target, service_name = d[0], d[1], d[2]
            module = import_module('smpa.services')
            service_class = getattr(module, service_name)
            if callable(service_class):
                service = service_class()
            else:
                service = service_class

            prop = target
            results = []
            ids = getattr(self, field)
            for id in ids:
                results.append(service.get(id))
            # console.log(f'Setting {prop} on {instance} to {related}')
            setattr(self, prop, results)

    def _get_related(self):
        for field, service_name in self.related.items():
            try:
                module = import_module('smpa.services')
                service_class = getattr(module, service_name)
                if callable(service_class):
                    service = service_class()
                else:
                    service = service_class

                prop = field.replace('_id', '')
                id = getattr(self, field)
                related = service.get(id)
                # console.log(f'Setting {prop} on {self} to {related}')
                setattr(self, prop, related)
            except Exception as e:
                console.warn(e)

    def _get_backrefs(self):
        for d in self.backrefs:
            field, service_name = d[0], d[1]
            try:
                module = import_module('.'.join(__name__.split('.')[:-1]))
                service_class = getattr(module, service_name)
                if callable(service_class):
                    service = service_class()
                else:
                    service = service_class

                query = {field: str(self.id)}
                related = service.first(**query)
                prop = underscore(service.__model__.__name__)
                console.log(f'Setting {prop} on {self} to {related}')
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


###################################
# Types
###################################
