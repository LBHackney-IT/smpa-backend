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
from falcon_cors import CORS

# Application
from .config.settings import init_settings
from .helpers.swagger import init_swagger
from .helpers.startup import Startup
from .helpers.console import console
from .config.settings import Config
from .db.documentdb.connection import DocumentDB
from .db.documentdb.registry import model_registry

from .routes import init_routes, EXEMPT_ROUTES

from falcon_multipart.middleware import MultipartMiddleware
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend


def user_loader(*args, **kwargs):
    from .services.user import _users
    try:
        uid = args[0]['user']['id']
        user = _users.get(uid)
    except Exception as e:
        try:
            email = args[0]['user']['subject']
            user = _users.first(email=email)
        except Exception as e:
            console.error(e)
            raise

    return user


secret_key = os.environ.get('SECRET_KEY')
auth_backend = JWTAuthBackend(user_loader, secret_key)
auth_middleware = FalconAuthMiddleware(
    auth_backend,
    exempt_routes=EXEMPT_ROUTES,
    exempt_methods=['HEAD']
)

# Setup CORS
cors = CORS(
    allow_origins_list=[
        'http://localhost:8081'
    ], allow_all_headers=True,
    allow_all_methods=True
)

# Create the Falcon app
# api = application = falcon.API()  # NO AUTH
api = application = falcon.API(middleware=[
    cors.middleware,
    auth_middleware,
    MultipartMiddleware()
])
api.req_options.auto_parse_form_urlencoded = True


config: Config
# db: RethinkDB
db: DocumentDB


def create_app():
    global config
    global db
    global api
    global application
    settings = init_settings()
    config = settings

    # Ensure the DB is set up
    # db = RethinkDB()
    # db.init()
    # model_registry.init()

    # Ensure the DocumentDB is set up
    db = DocumentDB(config)
    db = db.init()
    model_registry.init()

    # Set up initial data and routes
    Startup.init_data()
    init_routes(api, config)

    return api


create_app()
spec = init_swagger(api, config)
console.success('READY')
