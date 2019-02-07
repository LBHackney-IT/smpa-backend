# -*- coding: utf-8 -*-

"""
    smpaf.app
    ~~~~~~~~~
    Falcon Framework app

    Run a dev server with...

    ``gunicorn --reload smpaf.app -b 0.0.0.0:5000``
"""

__version__ = "0.2.2"

# 3rd party
import falcon

# Module
from .rdb.connection import RethinkDB
from .rdb.registry import model_registry
from .resources import (
    TestResource,
    AreaUnitResource, LinearUnitResource,
    UserResource, AgentResource, ApplicantResource,
    AddressResource, SiteAddressResource, BS7666AddressResource, ExternalAddressResource,
    InternationalAddressResource,
    DocumentSizeResource
)

# Create the Falcon app
api = application = falcon.API()


def init_route(path, resource):
    prefix = '/api/v1'
    api.add_route(f'{prefix}{path}', resource)


def create_app():
    # Ensure the DB is set up
    db = RethinkDB()
    db.init()
    model_registry.init()

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

    # Routes
    init_route('/tests', tests)
    init_route('/tests/{id}', tests)

    init_route('/area-units', area_units)
    init_route('/area-units/{id}', area_units)

    init_route('/linear-units', linear_units)
    init_route('/linear-units/{id}', linear_units)

    init_route('/users', users)
    init_route('/users/{id}', users)

    init_route('/agents', agents)
    init_route('/agents/{id}', agents)

    init_route('/applicants', applicants)
    init_route('/applicants/{id}', applicants)

    init_route('/addresses', addresses)
    init_route('/addresses/{id}', addresses)

    init_route('/site-addresses', siteaddresses)
    init_route('/site-addresses/{id}', siteaddresses)

    init_route('/bs7666-addresses', bs7666addresses)
    init_route('/bs7666-addresses/{id}', bs7666addresses)

    init_route('/external-addresses', externaladdresses)
    init_route('/external-addresses/{id}', externaladdresses)

    init_route('/external-addresses', externaladdresses)
    init_route('/external-addresses/{id}', externaladdresses)

    init_route('/international-addresses', internationaladdresses)
    init_route('/international-addresses/{id}', internationaladdresses)

    init_route('/document-sizes', documentsizes)
    init_route('/document-sizes/{id}', documentsizes)


create_app()
