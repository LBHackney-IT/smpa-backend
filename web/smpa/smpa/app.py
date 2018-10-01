# -*- coding: utf-8 -*-

"""
    smpa.app
    ~~~~~~~~
    This is the main WSGI app that Gunicorn runs.

    For local development you can just run...

    ``gunicorn --reload smpa.app:app -b 0.0.0.0:5000``

    http POST 0.0.0.0:5000/todos Authorization:"Bearer secret" description="Todo description"
"""

from .factory import create_app


app = create_app()
