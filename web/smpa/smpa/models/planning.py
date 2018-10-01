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


class MaxAnnualOperationalThroughput(BaseModel):
    __tablename__ = 'max_annual_operational_throughputs'

    volume_unit = sa.Column(Unicode(255))


class InertLandfill(BaseModel):
    __tablename__ = 'inter_landfills'

    total_void_capacity =
    max_annual_operational_throughput = sa.Column(
        sa.Integer, sa.ForeignKey('max_annual_operational_throughput.id'))
