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
    # Unit resources
    AreaUnitResource, AreaUnitListResource, LinearUnitResource, LinearUnitListResource,
    # User resources
    UserResource, AgentResource, ApplicantResource, AuthResource,
    # Address resources
    AddressPatch, AddressPost, SiteAddressPatch, SiteAddressPost,
    BS7666AddressResource, ExternalAddressResource, InternationalAddressResource,
    # Document size resources
    DocumentSizeResource,
    # Application resources
    ApplicationResource, ApplicationListResource,
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
    api.add_static_route("/redoc", os.path.join(
        os.path.dirname(__file__), "static", "redoc"))
    api.add_static_route("/swagger", os.path.join(
        os.path.dirname(__file__), "static", "swagger"))

    # Resources
    auth = AuthResource()
    addresses_patch = AddressPatch()
    addresses_post = AddressPost()
    siteaddresses_patch = SiteAddressPatch()
    siteaddresses_post = SiteAddressPost()
    applications = ApplicationResource()
    applications_list = ApplicationListResource()
    area_units = AreaUnitResource()
    area_units_list = AreaUnitListResource()
    linear_units = LinearUnitResource()
    linear_units_list = LinearUnitListResource()
    users = UserResource()
    agents = AgentResource()
    # applicants = ApplicantResource()
    documentsizes = DocumentSizeResource()
    material_option_roof_resource = MaterialOptionRoofResource()
    material_option_wall_resource = MaterialOptionWallResource()
    material_option_door_resource = MaterialOptionDoorResource()
    material_option_window_resource = MaterialOptionWindowResource()

    # Routes
    add_route(api, '/auth', auth)

    add_route(api, '/addresses', addresses_post)
    add_route(api, '/addresses/{id}', addresses_patch)

    add_route(api, '/area-units', area_units_list)
    add_route(api, '/area-units/{id}', area_units)

    add_route(api, '/linear-units', linear_units_list)
    add_route(api, '/linear-units/{id}', linear_units)

    add_route(api, '/applications', applications_list)
    add_route(api, '/applications/{id}', applications)

    add_route(api, '/users', users)
    add_route(api, '/users/{id}', users)

    add_route(api, '/agents', agents)
    add_route(api, '/agents/{id}', agents)

    # add_route(api, '/applicants', applicants)
    # add_route(api, '/applicants/{id}', applicants)

    add_route(api, '/site-addresses', siteaddresses_post)
    add_route(api, '/site-addresses/{id}', siteaddresses_patch)

    add_route(api, '/document-sizes', documentsizes)
    add_route(api, '/document-sizes/{id}', documentsizes)

    add_route(api, '/materials/options/roof', material_option_roof_resource)
    add_route(api, '/materials/options/wall', material_option_wall_resource)
    add_route(api, '/materials/options/door', material_option_door_resource)
    add_route(api, '/materials/options/window', material_option_window_resource)

    config.resources = [
        addresses_post,
        addresses_patch,
        siteaddresses_post,
        siteaddresses_patch,
        area_units,
        area_units_list,
        linear_units_list,
        linear_units,
        users,
        agents,
        # applicants,
        documentsizes,
        auth,
        material_option_roof_resource,
        material_option_wall_resource,
        material_option_door_resource,
        material_option_window_resource,
        applications_list,
        applications,
    ]
