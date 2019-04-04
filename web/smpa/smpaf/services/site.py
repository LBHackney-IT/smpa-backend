# -*- coding: utf-8 -*-

"""
    services.site
    ~~~~~~~~~~~~~
    Services for site models.
"""

from .rethink import RService

from ..models.site import SiteArea, SiteConstraints


class SiteAreaService(RService):
    __model__ = SiteArea


class SiteConstraintsService(RService):
    __model__ = SiteConstraints


_site_areas = SiteAreaService()
_site_constraints = SiteConstraintsService()
