# -*- coding: utf-8 -*-

"""
    models.proposal
    ~~~~~~~~~~~~~~~
    Models for describing a planning proposal.
"""


# 3rd party
import sqlalchemy as sa
from sqlalchemy_utils import ArrowType
from sqlalchemy.ext.associationproxy import association_proxy

# Project
from ..helpers.database import MyUUID

# Module
from .core import BaseModel


class BaseProposal(BaseModel):
    __abstract__ = True

    site_area = sa.Column(MyUUID, sa.ForeignKey('site_areas.id'))
    already_completed = sa.Column(sa.Boolean(), default=False)
    date_completed = sa.Column(ArrowType)
