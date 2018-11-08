# -*- coding: utf-8 -*-

"""
    smpa.conf
    ~~~~~~~~~
    Config for the application factory.
"""


# stdlib
import os

# 3rd party
from molten.contrib.prometheus import expose_metrics, prometheus_middleware  # NOQA
from molten import (
    Route, JSONParser, MultiPartParser, SettingsComponent, URLEncodingParser,
    ResponseRendererMiddleware
)
from molten.contrib.sqlalchemy import (
    SQLAlchemyMiddleware, SQLAlchemyEngineComponent, SQLAlchemySessionComponent
)

# Project
from .core.routes import get_docs, get_schema, debug_schema, debugger  # NOQA
from .resources.address import (
    AddressManagerComponent, AddressHandler, SiteAddressHandler, SiteAddressManagerComponent
)
from .resources.user import (
    AgentManagerComponent, AgentHandler, ApplicantHandler, ApplicantManagerComponent
)
from .resources.application import (
    PlanningApplicationManagerComponent, PlanningApplicationHandler
)

from .settings.base import EnvSettings
from .middleware.auth import AuthorizationMiddleware  # NOQA


settings = EnvSettings().get_settings(os.environ.get('SERVER_ENV'))


COMPONENTS = [
    SQLAlchemyEngineComponent(),
    SQLAlchemySessionComponent(),
    SettingsComponent(settings),
    AddressManagerComponent(),
    SiteAddressManagerComponent(),
    AgentManagerComponent(),
    ApplicantManagerComponent(),
    PlanningApplicationManagerComponent(),
]

MIDDLEWARE = [
    ResponseRendererMiddleware(),
    # AuthorizationMiddleware,
    SQLAlchemyMiddleware(),
]

ROUTES = [
    SiteAddressHandler.routes(),
    AddressHandler.routes(),
    AgentHandler.routes(),
    ApplicantHandler.routes(),
    PlanningApplicationHandler.routes(),
    Route("/_docs", get_docs),
    Route("/_schema", get_schema),
    # Route("/_schema", debug_schema),
    Route("/_debugger", debugger),
]

PARSERS = [
    JSONParser(),
    URLEncodingParser(),
    MultiPartParser(),
]


# Dev-only settings
# if os.environ.get('SERVER_ENV', 'development') == 'development':
#     MIDDLEWARE += [prometheus_middleware, ]
#     ROUTES += [Route("/_metrics", expose_metrics), ]
