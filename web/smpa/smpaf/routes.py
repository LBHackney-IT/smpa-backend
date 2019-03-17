# -*- coding: utf-8 -*-

"""
    smpaf.routes
    ~~~~~~~~~~~~~~~~
    Routing config.
"""


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
]


def add_route(api, path, resource):
    prefix = '/api/v1'
    api.add_route(f'{prefix}{path}', resource)


def init_routes(api):
    # Resources
    tests = TestResource()
    area_units = AreaUnitResource()
    linear_units = LinearUnitResource()
    users = UserResource()
    agents = AgentResource()
    applicants = ApplicantResource()
    addresses = AddressResource()
    siteaddresses = SiteAddressResource()
    bs7666addresses = BS7666AddressResource()
    externaladdresses = ExternalAddressResource()
    internationaladdresses = InternationalAddressResource()
    documentsizes = DocumentSizeResource()
    auth = AuthResource()

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
