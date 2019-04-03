# -*- coding: utf-8 -*-

"""
    helpers.startup
    ~~~~~~~~~~~~~~~
    Stuff for handling application start.
"""
import arrow
from .console import console
from ..config.defaults import (
    AREA_UNITS, LINEAR_UNITS, DOCUMENT_SIZES, ROLES, SUPERADMIN_USERS, WORKS_LOCATIONS,
    BASEMENT_WORKS_LOCATIONS, MATERIALS_ROOF, MATERIALS_WALL, MATERIALS_WINDOW, MATERIALS_DOOR
)
from ..services import (
    _area_units, _linear_units, _document_sizes, _roles, _users, _works_locations,
    _basement_works_locations, _material_options_roof, _material_options_wall,
    _material_options_window, _material_options_door
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
        for _ in BASEMENT_WORKS_LOCATIONS:
            _basement_works_locations.get_or_create(name=_)

        self._add_materials()
        self._add_users()
        # self._dummy_data()

        console.success('Created default data')

    @classmethod
    def _add_materials(self):
        for _ in MATERIALS_ROOF:
            _material_options_roof.get_or_create(name=_)
        for _ in MATERIALS_WALL:
            _material_options_wall.get_or_create(name=_)
        for _ in MATERIALS_WINDOW:
            _material_options_window.get_or_create(name=_)
        for _ in MATERIALS_DOOR:
            _material_options_door.get_or_create(name=_)

    @classmethod
    def _add_users(self):
        super_admin = _roles.first(name='SuperAdmin')
        for _ in SUPERADMIN_USERS:
            _users.get_or_create(
                email=_['email'],
                password=_['password'],
                role_id=str(super_admin.id)
            )

    @classmethod
    def _dummy_data(self):
        from ..services import _applications, _site_addresses
        u = _users.first()
        a = _applications.new(
            id='9e7cf43a-6860-4061-b585-65b4fb778a30',
            works_started=True,
            date_works_started='2017-01-01',
            works_completed=False,
            date_works_completed='2018-01-01',
            works_description="I did a thing to my house",
            owner_id=u.id
        )
        _applications.save(a)
        site_address = _site_addresses.new(
            id='dcde565b-ff0b-4177-9c0b-f3d8d131ce02',
            application_id=a.id,
            address_line_1="12 Stephen Mews",
            town_city="London",
            postcode="W1T 1AH",
            description="Hactar Towers"
        )
        _site_addresses.save(site_address)
