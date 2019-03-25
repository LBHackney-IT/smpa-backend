# -*- coding: utf-8 -*-

"""
    helpers.startup
    ~~~~~~~~~~~~~~~
    Stuff for handling application start.
"""

from .console import console
from ..config.defaults import (
    AREA_UNITS, LINEAR_UNITS,
    # DOCUMENT_SIZES, ROLES, SUPERADMIN_USERS, WORKS_LOCATIONS,
    # BASEMENT_WORKS_LOCATIONS, MATERIALS_ROOF, MATERIALS_WALL, MATERIALS_WINDOW, MATERIALS_DOOR
)
from ..services import (
    _area_units, _linear_units,
    # _document_sizes, _roles, _users, _works_locations,
    # _basement_works_locations, _material_options_roof, _material_options_wall,
    # _material_options_window, _material_options_door
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
        # for _ in DOCUMENT_SIZES:
        #     _document_sizes.get_or_create(name=_)
        # for _ in ROLES:
        #     _roles.get_or_create(name=_)
        # for _ in WORKS_LOCATIONS:
        #     _works_locations.get_or_create(name=_)
        # for _ in BASEMENT_WORKS_LOCATIONS:
        #     _basement_works_locations.get_or_create(name=_)

        self._add_materials()
        self._add_users()

        console.success('Created default data')

    @classmethod
    def _add_materials(self):
        pass
        # for _ in MATERIALS_ROOF:
        #     _material_options_roof.get_or_create(name=_)
        # for _ in MATERIALS_WALL:
        #     _material_options_wall.get_or_create(name=_)
        # for _ in MATERIALS_WINDOW:
        #     _material_options_window.get_or_create(name=_)
        # for _ in MATERIALS_DOOR:
        #     _material_options_door.get_or_create(name=_)

    @classmethod
    def _add_users(self):
        pass
        # super_admin = _roles.first(name='SuperAdmin')
        # for _ in SUPERADMIN_USERS:
        #     _users.get_or_create(
        #         email=_['email'],
        #         password=_['password'],
        #         role_id=str(super_admin.id)
        #     )
