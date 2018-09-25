# -*- coding: utf-8 -*-

"""
    models.core
    ~~~~~~~~~~~
    Core models and model related code.
"""

from __future__ import absolute_import, unicode_literals

import sqlalchemy.sql.sqltypes as types
from sqlalchemy import (
    Column, Table, func
)
from sqlalchemy.orm import mapper, class_mapper, backref, relation
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base

from ..helpers.database import MyUUID


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    __table_args__ = {'extend_existing': True}

    id = Column(MyUUID(), server_default=func.uuid_generate_v4(), primary_key=True)

    created_at = Column(types.DateTime, default=func.now())
    updated_at = Column(types.DateTime, default=func.now(), onupdate=func.now())

    def __str__(self):
        identifier = self.id
        if self.id is None:
            identifier = 'unsaved'
        if hasattr(self, 'slug'):
            identifier = self.slug
        elif hasattr(self, 'name'):
            identifier = self.name

        return f'<{self.__class__.__name__}: {identifier}>'

    def __repr__(self):
        return self.__str__()


####################################################################################################
# # Polymorphic association thing. Allows us to have a model that could belong to
# more than one parent. For instance, Link could belong to a freelancer or a
# supplier. Notes could belong to all sorts.
#
# See: http://techspot.zzzeek.org/files/2007/poly_assoc_3.py
# And: http://techspot.zzzeek.org/2007/05/29/polymorphic-associations-with-sqlalchemy/
####################################################################################################


def association(cls, table):
    """create an association 'interface'."""

    interface_name = table.name
    attr_name = "%s_rel" % interface_name

    metadata = table.metadata
    association_table = Table(
        "%s_associations" % interface_name, metadata,
        Column('assoc_id', types.Integer, primary_key=True),
        Column('type', types.Unicode(50), nullable=False)
    )

    class GenericAssoc(object):
        def __init__(self, name):
            self.type = name

    def interface(cls, name, uselist=True):

        mapper = class_mapper(cls)
        table = mapper.local_table
        mapper.add_property(
            attr_name, relation(
                GenericAssoc, backref=backref('_backref_%s' % table.name, uselist=False)))

        if uselist:
            # list based property decorator
            def get(self):
                if getattr(self, attr_name) is None:
                    setattr(self, attr_name, GenericAssoc(table.name))
                return getattr(self, attr_name).targets
            setattr(cls, name, property(get))
        else:
            # scalar based property decorator
            def get(self):
                return getattr(self, attr_name).targets[0]

            def set(self, value):
                if getattr(self, attr_name) is None:
                    setattr(self, attr_name, GenericAssoc(table.name))
                getattr(self, attr_name).targets = [value]
            setattr(cls, name, property(get, set))

    setattr(cls, 'member', property(
        lambda self: getattr(self.association, '_backref_%s' % self.association.type)))

    mapper(GenericAssoc, association_table, properties={
        'targets': relation(cls, backref='association'),
    })

    return interface
