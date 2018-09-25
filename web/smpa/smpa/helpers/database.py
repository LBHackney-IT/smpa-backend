# -*- coding: utf-8 -*-

"""
    helpers.database
    ~~~~~~~~~~~~~~~~
    Mixins and stuff for helping with models
"""

import uuid

from sqlalchemy import (
    Table, Column, Boolean, Integer, Unicode, DateTime, ForeignKey, UnicodeText, func, event
)
from sqlalchemy.types import CHAR, TypeDecorator
from sqlalchemy_utils import ArrowType
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.dialects.postgresql import UUID


class MyUUID(TypeDecorator):
    """Platform-independent GUID type.

    Uses Postgresql's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.

    From here:
    http://docs.sqlalchemy.org/en/rel_0_9/core/custom_types.html#backend-agnostic-guid-type

    """
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return "%.32x" % uuid.UUID(value)
            else:
                # hexstring
                return "%.32x" % value

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return uuid.UUID(value)


###############################################################################
# MODEL MIXINS
###############################################################################


class TrackMixin(object):
    """Store who added an object"""
    __table_args__ = {'extend_existing': True}

    @declared_attr
    def creator_id(cls):
        return db.Column(MyUUID(), db.ForeignKey('user.id'), nullable=True)

    @declared_attr
    def creator(cls):
        return db.relation('User', primaryjoin='%s.creator_id == User.id' % cls.__name__)

    @declared_attr
    def editor_id(cls):
        return db.Column(MyUUID(), db.ForeignKey('user.id'), nullable=True)

    @declared_attr
    def editor(cls):
        return db.relation('User', primaryjoin='%s.editor_id == User.id' % cls.__name__)


class JsonSerializer(object):
    """A mixin that can be used to mark a SQLAlchemy model class which
    implements a :func:`to_json` method. The :func:`to_json` method is used
    in conjuction with the custom :class:`JSONEncoder` class. By default this
    mixin will assume all properties of the SQLAlchemy model are to be visible
    in the JSON output. Extend this class to customize which properties are
    public, hidden or modified before being being passed to the JSON serializer.
    """

    __json_public__ = None
    __json_hidden__ = None
    __json_modifiers__ = None

    def get_field_names(self):
        for p in self.__mapper__.iterate_properties:
            yield p.key

    def to_json(self):
        field_names = self.get_field_names()

        public = self.__json_public__ or field_names
        hidden = self.__json_hidden__ or []
        modifiers = self.__json_modifiers__ or dict()

        rv = dict()
        for key in public:
            rv[key] = getattr(self, key)
        for key, modifier in list(modifiers.items()):
            value = getattr(self, key)
            rv[key] = modifier(value, self)
        for key in hidden:
            rv.pop(key, None)
        return rv
