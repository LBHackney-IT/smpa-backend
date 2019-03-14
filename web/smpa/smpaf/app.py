# -*- coding: utf-8 -*-

"""
    smpaf.app
    ~~~~~~~~~
    Falcon Framework app

    Run a dev server with...

    ``gunicorn --reload smpaf.app -b 0.0.0.0:5000``
"""

__version__ = "0.2.2"

import os

# 3rd party
import falcon

# Application
from .helpers.startup import Startup
from .rdb.connection import RethinkDB
from .rdb.registry import model_registry
from .routes import init_routes, EXEMPT_ROUTES

from falcon_auth import FalconAuthMiddleware, JWTAuthBackend


user_loader = lambda email, password: {'email': email}
secret_key = os.environ.get('SECRET_KEY')
auth_backend = JWTAuthBackend(user_loader, secret_key)
auth_middleware = FalconAuthMiddleware(
    auth_backend,
    exempt_routes=EXEMPT_ROUTES,
    exempt_methods=['HEAD']
)

# Create the Falcon app
api = application = falcon.API(middleware=[auth_middleware])
# api = application = falcon.API()


def create_app():
    # Ensure the DB is set up
    db = RethinkDB()
    db.init()
    model_registry.init()
    Startup.init_data()
    init_routes(api)


create_app()