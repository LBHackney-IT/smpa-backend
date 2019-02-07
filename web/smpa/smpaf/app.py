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
from .routes import init_routes

# Create the Falcon app
api = application = falcon.API()


def create_app():
    # Ensure the DB is set up
    db = RethinkDB()
    db.init()
    model_registry.init()
    init_routes(api)


create_app()
