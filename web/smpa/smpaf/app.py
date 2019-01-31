# -*- coding: utf-8 -*-

"""
    smpaf.app
    ~~~~~~~~~
    Falcon Framework app

    Run a dev server with...

    ``gunicorn --reload smpaf.app -b 0.0.0.0:5000``
"""

# 3rd party
import falcon

# Module
from .rdb.connection import RethinkDB
from .rdb.registry import model_registry
from .middleware.db import SQLAlchemySessionManager
from .resources.test import TestResource
from .resources.unit import AreaUnitResource, LinearUnitResource
from .resources.user import UserResource, AgentResource, ApplicantResource
from .resources.address import (
    AddressResource, SiteAddressResource, BS7666AddressResource, ExternalAddressResource,
    InternationalAddressResource
)
from .resources.document import DocumentSizeResource


# Create the Falcon app
api = application = falcon.API()


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
    api.add_route('/tests', tests)
    api.add_route('/tests/{id}', tests)

    api.add_route('/area-units', area_units)
    api.add_route('/area-units/{id}', area_units)

    api.add_route('/linear-units', linear_units)
    api.add_route('/linear-units/{id}', linear_units)

    api.add_route('/users', users)
    api.add_route('/users/{id}', users)

    api.add_route('/agents', agents)
    api.add_route('/agents/{id}', agents)

    api.add_route('/addresses', addresses)
    api.add_route('/addresses/{id}', addresses)

    api.add_route('/site-addresses', siteaddresses)
    api.add_route('/site-addresses/{id}', siteaddresses)

    api.add_route('/bs7666-addresses', bs7666addresses)
    api.add_route('/bs7666-addresses/{id}', bs7666addresses)

    api.add_route('/external-addresses', externaladdresses)
    api.add_route('/external-addresses/{id}', externaladdresses)

    api.add_route('/external-addresses', externaladdresses)
    api.add_route('/external-addresses/{id}', externaladdresses)

    api.add_route('/international-addresses', internationaladdresses)
    api.add_route('/international-addresses/{id}', internationaladdresses)

    api.add_route('/document-sizes', documentsizes)
    api.add_route('/document-sizes/{id}', documentsizes)


create_app()
