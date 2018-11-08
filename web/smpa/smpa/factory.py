# -*- coding: utf-8 -*-

"""
    smpa.factory
    ~~~~~~~~~~~~
    App factory.
"""

# 3rd party
from wsgicors import CORS
from molten import App

# Project
from .conf import (
    COMPONENTS,
    MIDDLEWARE,
    ROUTES,
    PARSERS,
    settings
)


def create_app() -> App:
    app = App(
        components=COMPONENTS,
        middleware=MIDDLEWARE,
        routes=ROUTES,
        parsers=PARSERS,
    )

    app.settings = settings

    return CORS(app, headers="*", methods="*", origin="*", maxage="86400")
