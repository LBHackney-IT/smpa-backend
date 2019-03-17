# -*- coding: utf-8 -*-

"""
    helpers.startup
    ~~~~~~~~~~~~~~~
    Stuff for handling application start.
"""

from .console import console
from ..config.defaults import (
    AREA_UNITS, LINEAR_UNITS, DOCUMENT_SIZES, ROLES, SUPERADMIN_USERS, WORKS_LOCATIONS
)
from ..services import (
    _area_units, _linear_units, _document_sizes, _roles, _users, _works_locations
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
        for _ in DOCUMENT_SIZES:
            _document_sizes.get_or_create(name=_)
        for _ in ROLES:
            _roles.get_or_create(name=_)
        for _ in WORKS_LOCATIONS:
            _works_locations.get_or_create(name=_)

        super_admin = _roles.first(name='SuperAdmin')
        for _ in SUPERADMIN_USERS:
            _users.get_or_create(
                email=_['email'],
                password=_['password'],
                role_id=str(super_admin.id)
            )

        console.success('Created default data')
