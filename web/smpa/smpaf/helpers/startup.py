# -*- coding: utf-8 -*-

"""
    helpers.startup
    ~~~~~~~~~~~~~~~
    Stuff for handling application start.
"""

from .console import console
from ..config.defaults import AREA_UNITS, LINEAR_UNITS
from ..services import (
    _area_units, _linear_units
)


class Startup:

    @classmethod
    def init_data(self):
        """Creates some initital data. Called at startup, objects should be idempotent.
        """
        for _ in AREA_UNITS:
            _area_units.get_or_create(name=_)
        for _ in LINEAR_UNITS:
            _linear_units.get_or_create(name=_)

        console.success('Created default data')
