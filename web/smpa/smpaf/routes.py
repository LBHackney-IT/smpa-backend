# -*- coding: utf-8 -*-

"""
    smpaf.routes
    ~~~~~~~~~~~~~~~~
    Routing config.
"""
import os
from .resources.swagger import ApiSpecResource

from .resources.material import (
    MaterialOptionRoofResource,
    MaterialOptionWallResource,
    MaterialOptionWindowResource,
    MaterialOptionDoorResource,
)
from .resources import (
    TestResource,
    AreaUnitResource, LinearUnitResource,
    UserResource, AgentResource, ApplicantResource, AuthResource,
    AddressResource, SiteAddressResource, BS7666AddressResource, ExternalAddressResource,
    InternationalAddressResource,
    DocumentSizeResource
)

EXEMPT_ROUTES = [
    '/auth',
    '/docs'
]


def add_route(api, path, resource):
    prefix = '/api/v1'
    api.add_route(f'{prefix}{path}', resource)


def init_routes(api, config):
    # Documentation routes
    api.add_route("/apispec", ApiSpecResource())
    api.add_static_route("/swagger", os.path.join(os.path.dirname(__file__), "static"))

    # Resources
    tests = TestResource()
    area_units = AreaUnitResource()
    linear_units = LinearUnitResource()
    users = UserResource()
    agents = AgentResource()
    applicants = ApplicantResource()
    siteaddresses = SiteAddressResource()
    documentsizes = DocumentSizeResource()
    auth = AuthResource()
    material_option_roof_resource = MaterialOptionRoofResource()
    material_option_wall_resource = MaterialOptionWallResource()
    material_option_door_resource = MaterialOptionDoorResource()
    material_option_window_resource = MaterialOptionWindowResource()

    # Routes
    add_route(api, '/auth', auth)

    add_route(api, '/tests', tests)
    add_route(api, '/tests/{id}', tests)

    add_route(api, '/area-units', area_units)
    add_route(api, '/area-units/{id}', area_units)

    add_route(api, '/linear-units', linear_units)
    add_route(api, '/linear-units/{id}', linear_units)

    add_route(api, '/users', users)
    add_route(api, '/users/{id}', users)

    add_route(api, '/agents', agents)
    add_route(api, '/agents/{id}', agents)

    add_route(api, '/applicants', applicants)
    add_route(api, '/applicants/{id}', applicants)

    add_route(api, '/site-addresses', siteaddresses)
    add_route(api, '/site-addresses/{id}', siteaddresses)

    add_route(api, '/document-sizes', documentsizes)
    add_route(api, '/document-sizes/{id}', documentsizes)

    add_route(api, '/materials/options/roof', material_option_roof_resource)
    add_route(api, '/materials/options/wall', material_option_wall_resource)
    add_route(api, '/materials/options/door', material_option_door_resource)
    add_route(api, '/materials/options/window', material_option_window_resource)

    config.resources = [
        tests,
        area_units,
        linear_units,
        users,
        agents,
        applicants,
        siteaddresses,
        documentsizes,
        auth,
        material_option_roof_resource,
        material_option_wall_resource,
        material_option_door_resource,
        material_option_window_resource,
    ]
