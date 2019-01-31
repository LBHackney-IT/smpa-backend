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
from .resources.images import ImageResource
from .resources.things import ThingsResource
from .resources.unit import AreaUnitResource, LinearUnitResource


# Create the Falcon app
api = application = falcon.API()


def create_app():
    # Ensure the DB is set up
    db = RethinkDB()
    db.init()
    model_registry.init()

    # Resources
    things = ThingsResource()
    images = ImageResource()
    tests = TestResource()
    area_units = AreaUnitResource()
    linear_units = LinearUnitResource()

    # Routes
    api.add_route('/tests', tests)
    api.add_route('/tests/{id}', tests)

    api.add_route('/area-units', area_units)
    api.add_route('/area-units/{id}', area_units)

    api.add_route('/linear-units', linear_units)
    api.add_route('/linear-units/{id}', linear_units)


create_app()
