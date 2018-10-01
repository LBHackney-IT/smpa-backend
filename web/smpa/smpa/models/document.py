# -*- coding: utf-8 -*-

"""
    models.document
    ~~~~~~~~~~~~~~~
    Document related models.
"""

# 3rd party
import sqlalchemy as sa
from sqlalchemy.ext.associationproxy import association_proxy  # NOQA

# Project
from ..helpers.database import MyUUID

# Module
from .core import BaseModel


class DocumentSize(BaseModel):

    """For storing document sizes. Although why anyone would need to do this
    in 2018 remains to be seen.

    Attributes:
        name (Unicode): The size, ie: A4, A3 etc.
    """

    __tablename__ = 'document_sizes'

    name = sa.Column(sa.Unicode(20), nullable=False)
