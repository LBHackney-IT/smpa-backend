# -*- coding: utf-8 -*-

"""
    models.user
    ~~~~~~~~~~~
    User models.
"""

# 3rd party
from sqlalchemy import Column, String, Integer, ForeignKey, Unicode

# Module
from .core import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    first_name = Column(Unicode(255))
    last_name = Column(Unicode(255))

    def __str__(self):
        return f'<User: {self.first_name} {self.last_name}>'


class PersonName(BaseModel):
    __tablename__ = 'person_name'

    title = Column(Unicode(255))
    given_name = Column(Unicode(255))
    family_name = Column(Unicode(255))

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.title} {self.given_name} {self.family_name}>'

