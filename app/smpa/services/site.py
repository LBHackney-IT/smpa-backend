# -*- coding: utf-8 -*-

"""
    services.site
    ~~~~~~~~~~~~~
    Services for site models.
"""

from .mongo import DService

from ..models.site import SiteArea, SiteConstraints


class SiteAreaService(DService):
    __model__ = SiteArea


class SiteConstraintsService(DService):
    __model__ = SiteConstraints


_site_areas = SiteAreaService()
_site_constraints = SiteConstraintsService()
