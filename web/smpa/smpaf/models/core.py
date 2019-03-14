# -*- coding: utf-8 -*-

"""
    smpa.models.core
    ~~~~~~~~~~~~~~~~
    BaseModel class
"""

import datetime
from schematics.models import Model, ModelMeta
from inflection import tableize
from schematics.types import (
    StringType, BooleanType, DateTimeType, IntType, UUIDType
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

    id = UUIDType()
    created_at = DateTimeType(default=datetime.datetime.now)
    updated_at = DateTimeType(default=datetime.datetime.now)

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


# # -*- coding: utf-8 -*-

# """
#     models.core
#     ~~~~~~~~~~~
#     Core models and model related code.
# """

# from __future__ import absolute_import, unicode_literals

# import arrow
# import sqlalchemy.sql.sqltypes as types
# from sqlalchemy import (
#     Column, Table, func
# )
# from sqlalchemy_utils import ArrowType
# from sqlalchemy.orm import mapper, class_mapper, backref, relation
# from sqlalchemy.ext.hybrid import hybrid_property
# from sqlalchemy.ext.associationproxy import association_proxy
# from sqlalchemy.ext.declarative import declarative_base

# from ..helpers.database import MyUUID


# Base = declarative_base()


# class BaseModel(Base):

#     """Abstract base model providing a UUID primary key, created_at and
#     updated_at timestamps.

#     Attributes:
#         id (MyUUID): Description
#         created_at (Arrow): Description
#         updated_at (Arrow): Description
#     """

#     __abstract__ = True
#     __table_args__ = {'extend_existing': True}

#     id = Column(MyUUID(), server_default=func.uuid_generate_v4(), primary_key=True)

#     created_at = Column(ArrowType, default=func.now())
#     updated_at = Column(ArrowType, default=func.now(), onupdate=func.now())

#     def __str__(self):
#         identifier = self.id
#         if self.id is None:
#             identifier = 'unsaved'
#         if hasattr(self, 'slug'):
#             identifier = self.slug
#         elif hasattr(self, 'name'):
#             identifier = self.name

#         return f'<{self.__class__.__name__}: {identifier}>'

#     def __repr__(self):
#         return self.__str__()


# ####################################################################################################
# # # Polymorphic association thing. Allows us to have a model that could belong to
# # more than one parent. For instance, Link could belong to a freelancer or a
# # supplier. Notes could belong to all sorts.
# #
# # See: http://techspot.zzzeek.org/files/2007/poly_assoc_3.py
# # And: http://techspot.zzzeek.org/2007/05/29/polymorphic-associations-with-sqlalchemy/
# ####################################################################################################


# def association(cls, table):
#     """create an association 'interface'."""

#     interface_name = table.name
#     attr_name = "%s_rel" % interface_name

#     metadata = table.metadata
#     association_table = Table(
#         "%s_associations" % interface_name, metadata,
#         Column('assoc_id', types.Integer, primary_key=True),
#         Column('type', types.Unicode(50), nullable=False)
#     )

#     class GenericAssoc(object):
#         def __init__(self, name):
#             self.type = name

#     def interface(cls, name, uselist=True):

#         mapper = class_mapper(cls)
#         table = mapper.local_table
#         mapper.add_property(
#             attr_name, relation(
#                 GenericAssoc, backref=backref('_backref_%s' % table.name, uselist=False)))

#         if uselist:
#             # list based property decorator
#             def get(self):
#                 if getattr(self, attr_name) is None:
#                     setattr(self, attr_name, GenericAssoc(table.name))
#                 return getattr(self, attr_name).targets
#             setattr(cls, name, property(get))
#         else:
#             # scalar based property decorator
#             def get(self):
#                 return getattr(self, attr_name).targets[0]

#             def set(self, value):
#                 if getattr(self, attr_name) is None:
#                     setattr(self, attr_name, GenericAssoc(table.name))
#                 getattr(self, attr_name).targets = [value]
#             setattr(cls, name, property(get, set))

#     setattr(cls, 'member', property(
#         lambda self: getattr(self.association, '_backref_%s' % self.association.type)))

#     mapper(GenericAssoc, association_table, properties={
#         'targets': relation(cls, backref='association'),
#     })

#     return interface
