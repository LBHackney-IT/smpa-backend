# -*- coding: utf-8 -*-

"""
    helpers.startup
    ~~~~~~~~~~~~~~~
    Stuff for handling application start.
"""
import os
import arrow
import bugsnag
from .console import console
from ..config.defaults import (
    AREA_UNITS, LINEAR_UNITS, DOCUMENT_SIZES, ROLES, SUPERADMIN_USERS, WORKS_LOCATIONS,
    BASEMENT_WORKS_TYPES, MATERIALS_ROOF, MATERIALS_WALL, MATERIALS_WINDOW, MATERIALS_DOOR,
    ROOF_WORKS_TYPES, BORDER_WORKS_TYPES, ACCESS_WORKS_TYPES, ACCESS_WORKS_SCOPES,
    PARKING_WORKS_SCOPES, EQUIPMENT_WORKS_TYPES, EQUIPMENT_WORKS_CONSERVATION_TYPES,
    GATES_FENCES_WALLS_TYPES, DOCUMENT_TYPES, DECLARATIONS, OWNERSHIP_TYPES, APPLICATION_STATUSES,
    STAGING_ADMIN_USERS
)
from ..services.application import _application_statuses
from ..services.unit import _area_units, _linear_units
from ..services.document import _document_sizes, _document_types
from ..services.user import _roles, _users
from ..services.meta import _declarations, _ownership_types
from ..services.work import (
    _works_locations, _basement_works_types, _roof_works_types, _border_works_types,
    _access_works_scopes, _access_works_types, _parking_works_scopes, _equipment_works_types,
    _equipment_works_conservation_types, _gates_fences_walls_types,
    # TODO
    _work_extension_options
)
from ..services.material import (
    _material_options_roof, _material_options_wall,
    _material_options_window, _material_options_door
)


class Startup:

    @classmethod
    def init_data(self):
        """Creates some initital data. Called at startup, objects should be idempotent.
        """
        for _ in AREA_UNITS:
            _area_units.get_or_create(id=_[0], name=_[1])
        for _ in LINEAR_UNITS:
            _linear_units.get_or_create(id=_[0], name=_[1])
        for _ in DOCUMENT_SIZES:
            _document_sizes.get_or_create(id=_[0], name=_[1])
        for _ in DOCUMENT_TYPES:
            _document_types.get_or_create(id=_[0], name=_[1])
        for _ in ROLES:
            _roles.get_or_create(id=_[0], name=_[1])
        for _ in WORKS_LOCATIONS:
            _works_locations.get_or_create(id=_[0], name=_[1])
        for _ in BASEMENT_WORKS_TYPES:
            _basement_works_types.get_or_create(id=_[0], name=_[1])
        for _ in ROOF_WORKS_TYPES:
            _roof_works_types.get_or_create(id=_[0], name=_[1])
        for _ in BORDER_WORKS_TYPES:
            _border_works_types.get_or_create(id=_[0], name=_[1])
        for _ in ACCESS_WORKS_TYPES:
            _access_works_types.get_or_create(id=_[0], name=_[1])
        for _ in ACCESS_WORKS_SCOPES:
            _access_works_scopes.get_or_create(id=_[0], name=_[1])
        for _ in PARKING_WORKS_SCOPES:
            _parking_works_scopes.get_or_create(id=_[0], name=_[1])
        for _ in EQUIPMENT_WORKS_TYPES:
            _equipment_works_types.get_or_create(id=_[0], name=_[1])
        for _ in EQUIPMENT_WORKS_CONSERVATION_TYPES:
            _equipment_works_conservation_types.get_or_create(id=_[0], name=_[1])
        for _ in GATES_FENCES_WALLS_TYPES:
            _gates_fences_walls_types.get_or_create(id=_[0], name=_[1])
        for _ in DECLARATIONS:
            _declarations.get_or_create(id=_[0], name=_[1])
        for _ in OWNERSHIP_TYPES:
            _ownership_types.get_or_create(id=_[0], name=_[1])
        for _ in APPLICATION_STATUSES:
            _application_statuses.get_or_create(id=_[0], name=_[1])

        self._add_materials()

        try:
            self._add_users()
        except Exception as e:
            console.error(e)

        from smpa.app import config
        if config.base == 'development' or config.base == 'test':
            try:
                self._dummy_data()
            except Exception as e:
                console.error(e)
                raise
            else:
                console.success('Created dummy data')

        console.success('Created default data')

    @classmethod
    def _add_materials(self):
        for _ in MATERIALS_ROOF:
            _material_options_roof.get_or_create(id=_[0], name=_[1])
        for _ in MATERIALS_WALL:
            _material_options_wall.get_or_create(id=_[0], name=_[1])
        for _ in MATERIALS_WINDOW:
            _material_options_window.get_or_create(id=_[0], name=_[1])
        for _ in MATERIALS_DOOR:
            _material_options_door.get_or_create(id=_[0], name=_[1])

    @classmethod
    def _add_users(self):
        super_admin = _roles.first(name='SuperAdmin')
        role_id = str(super_admin.id)
        for _ in SUPERADMIN_USERS:
            try:
                u = _users.get_or_create(
                    id=_['id'],
                    email=_['email'],
                    password=_['password'],
                    role_id=role_id
                )
                u.verified_at = arrow.utcnow().datetime
                _users.save(u)
            except Exception as e:
                bugsnag.notify(
                    e,
                    extra_data={
                        'id': _['id'],
                        'email': _['email'],
                        'user': u,
                    }, severity='warn'
                )
            else:
                bugsnag.notify(
                    Exception('SUPERADMIN CREATED'),
                    extra_data={
                        'id': _['id'],
                        'email': _['email'],
                        'user': u,
                    }, severity='info'
                )

        if os.environ.get('SERVER_ENV') == 'staging':
            for _ in STAGING_ADMIN_USERS:
                try:
                    u = _users.get_or_create(
                        id=_['id'],
                        email=_['email'],
                        password=_['password'],
                        role_id=role_id
                    )
                    u.verified_at = arrow.now().datetime
                    _users.save(u)
                except Exception as e:
                    bugsnag.notify(
                        e,
                        extra_data={
                            'id': _['id'],
                            'email': _['email'],
                            'user': u,
                        }, severity='warn'
                    )
                else:
                    bugsnag.notify(
                        Exception('STAGING USER CREATED'),
                        extra_data={
                            'id': _['id'],
                            'email': _['email'],
                            'user': u,
                        }, severity='info'
                    )

        console.log('Added admin users')

    @classmethod
    def _dummy_data(self):
        from ..services.application import _applications
        from ..services.address import _site_addresses
        user_role = _roles.first(name='User')
        if user_role is None:
            import ipdb; ipdb.set_trace()
        u = _users.get_or_create(
            id="b7d623db-5b4a-43df-b3f1-2bfca845d657",
            email="test@example.com",
            password="secretpassword",
            role_id=str(user_role.id),
            verified_at=arrow.utcnow().datetime
        )
        a = _applications.get_or_create(
            id='9e7cf43a-6860-4061-b585-65b4fb778a30'
        )
        if a is not None:
            a.works_started = True
            a.date_works_started = arrow.get('2017-01-01').date()
            a.works_completed = False
            a.date_works_completed = arrow.get('2018-01-01').date()
            a.works_description = "I did a thing to my house"
            a.owner_id = u.id
            _applications.save(a)
        else:
            console.warn("Failed to get or create Application")

        site_address = _site_addresses.get_or_create(
            id='dcde565b-ff0b-4177-9c0b-f3d8d131ce02'
        )

        if site_address is not None:
            site_address.application_id = str(a.id)
            site_address.address_line_1 = "12 Stephen Mews"
            site_address.town_city = "London"
            site_address.postcode = "W1T 1AH"
            site_address.description = "Hactar Towers"
            _site_addresses.save(site_address)
        else:
            console.warn("Failed to get or create site address")

        console.success('Added dummy data')
