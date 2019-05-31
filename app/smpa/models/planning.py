# # -*- coding: utf-8 -*-

# """
#     models.planning
#     ~~~~~~~~~~~~~~~
#     Planning specific models. This might get re-named or simply re-ordered.

#     TODO: Work out what these are
# """


# # 3rd Party
# import sqlalchemy as sa

# # Module
# from .core import BaseModel


# class MaxAnnualOperationalThroughput(BaseModel):
#     volume_unit = sa.Column(Unicode(255))


# class InertLandfill(BaseModel):
#     total_void_capacity =''
#     max_annual_operational_throughput = sa.Column(
#         sa.Integer, sa.ForeignKey('max_annual_operational_throughput.id'))
