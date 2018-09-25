# -*- coding: utf-8 -*-

"""
    models.planning
    ~~~~~~~~~~~~~~~
    Planning specific models. This might get re-named or simply re-ordered.
"""


# 3rd Party
import sqlalchemy as sa

# Module
from .core import BaseModel


class VolumeUnit(BaseModel):

    """Used for providing a predefined list of avaliable volume units.

    Attributes:
        unit (Unicode): The unit, eg: cubic meters
    """

    __tablename__ = 'volume_unit'

    unit = sa.Column(sa.Unicode(50))


class MaxAnnualOperationalThroughput(BaseModel):
    __tablename__ = 'max_annual_operational_throughput'

    volume_unit = sa.Column(sa.Integer, sa.ForeignKey('volume_unit.id'))


class InertLandfill(BaseModel):
    __tablename__ = 'inter_landfill'

    total_void_capacity
    max_annual_operational_throughput
