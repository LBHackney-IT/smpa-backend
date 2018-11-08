# -*- coding: utf-8 -*-

"""
    smpa.core.routes
    ~~~~~~~~~~~~~~~~
    Universal routes.
"""

from molten.openapi import Metadata, OpenAPIHandler, OpenAPIUIHandler, HTTPSecurityScheme


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
    import ipdb; ipdb.set_trace()  # NOQA
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
