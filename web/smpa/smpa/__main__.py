# -*- coding: utf-8 -*-

"""
    smpa.__main__
    ~~~~~~~~~~~~~
    Allows the application to be run as a module serving the WSGI application
    over waitress.

    To start the server ``python -m smpa``

    http POST 0.0.0.0:5000/todos Authorization:"Bearer secret" description="Todo description"

    Get the schema

    http 0.0.0.0:5000/_schema
"""

from waitress import serve
from .factory import create_app
import logging


# LOGGING
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)


# WSGI APP
app = create_app()


# SERVER
serve(app, listen='*:5000')
