# -*- coding: utf-8 -*-

"""
    services.application
    ~~~~~~~~~~~~~~~~
    Planning Application services.
"""

# from ..models.application import PlanningApplication

from .core import Service


class PlanningApplicationService(Service):
    __model__ = None


_planning_applications = PlanningApplicationService()
