# -*- coding: utf-8 -*-

"""
    smpa.factory
    ~~~~~~~~~~~~
    App factory.
"""

# stdlib
import os

# 3rd party
from molten import (
    App, Route, JSONParser, JSONRenderer, MultiPartParser, SettingsComponent, URLEncodingParser,
    ResponseRendererMiddleware, Include
)
from wsgicors import CORS
from molten.openapi import Metadata, OpenAPIHandler, OpenAPIUIHandler, HTTPSecurityScheme
from molten.contrib.sqlalchemy import (
    SQLAlchemyMiddleware, SQLAlchemyEngineComponent, SQLAlchemySessionComponent
)

# Module
# Application
from .settings.base import EnvSettings
from .resources.address import (
    AddressManagerComponent, AddressHandler, SiteAddressHandler, SiteAddressManagerComponent
)
from .resources.application import (
    PlanningApplicationManagerComponent, PlanningApplicationHandler
)
from .middleware.auth import AuthorizationMiddleware


get_docs = OpenAPIUIHandler()

get_schema = OpenAPIHandler(
    metadata=Metadata(
        title="Submit my Planning Application",
        description="An API for managing planning applications.",
        version="0.0.1",
    ),
    # security_schemes=[HTTPSecurityScheme("default", "bearer")],
    # default_security_scheme="default",
)


def debug_schema():
    import ipdb; ipdb.set_trace()
    return OpenAPIHandler(
        metadata=Metadata(
            title="Submit my Planning Application",
            description="An API for managing planning applications.",
            version="0.0.1",
        ),
        security_schemes=[HTTPSecurityScheme("default", "bearer")],
        default_security_scheme="default",
    )


def debugger():
    import ipdb
    ipdb.set_trace()


def create_app() -> App:
    settings = EnvSettings().get_settings(os.environ.get('SERVER_ENV'))

    app = App(
        components=[
            SQLAlchemyEngineComponent(),
            SQLAlchemySessionComponent(),
            SettingsComponent(settings),
            AddressManagerComponent(),
            SiteAddressManagerComponent(),
            PlanningApplicationManagerComponent(),
        ],
        middleware=[
            ResponseRendererMiddleware(),
            AuthorizationMiddleware,
            SQLAlchemyMiddleware(),
        ],
        routes=[
            SiteAddressHandler.routes(),
            AddressHandler.routes(),
            PlanningApplicationHandler.routes(),
            Route("/_docs", get_docs),
            Route("/_schema", get_schema),
            Route("/_debugger", debugger),
        ],
        parsers=[
            JSONParser(),
            URLEncodingParser(),
            MultiPartParser(),
        ],
    )

    app.settings = settings

    return CORS(app, headers="*", methods="*", origin="*", maxage="86400")
