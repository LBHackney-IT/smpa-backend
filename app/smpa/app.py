# -*- coding: utf-8 -*-

"""
    smpa.app
    ~~~~~~~~~
    Falcon Framework app

    Run a dev server with...

    ``gunicorn --reload smpa.app -b 0.0.0.0:5000``
    ``gunicorn --reload smpa.app -b 0.0.0.0:5000 -t 99999999``
"""

__version__ = "0.2.2"

import os

# 3rd party
import falcon

# Application
from .helpers.swagger import init_swagger
from .helpers.startup import Startup
from .helpers.console import console
from .config.settings import Config
from .rdb.connection import RethinkDB
from .rdb.registry import model_registry
from .routes import init_routes, EXEMPT_ROUTES

from falcon_auth import FalconAuthMiddleware, JWTAuthBackend


def user_loader(*args, **kwargs):
    from .services.user import _users
    try:
        uid = args[0]['user']['id']
        user = _users.get(uid)
    except Exception as e:
        console.error(e)
    else:
        return user


secret_key = os.environ.get('SECRET_KEY')
auth_backend = JWTAuthBackend(user_loader, secret_key)
auth_middleware = FalconAuthMiddleware(
    auth_backend,
    exempt_routes=EXEMPT_ROUTES,
    exempt_methods=['HEAD']
)

# Create the Falcon app
# api = application = falcon.API()  # NO AUTH
api = application = falcon.API(middleware=[auth_middleware])
api.req_options.auto_parse_form_urlencoded = True

config = Config()


def create_app():
    # Ensure the DB is set up
    db = RethinkDB()
    db.init()
    model_registry.init()
    Startup.init_data()
    init_routes(api, config)


create_app()
spec = init_swagger(api, config)