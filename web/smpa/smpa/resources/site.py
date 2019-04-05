import falcon

from typing import Optional

from ..schemas.core import CoreListSchema, CoreGetSchema  # NOQA
from .core import Resource, ListResource
from ..services.site import _site_areas, _site_constraints


class SiteAreaPostResource(ListResource):
    _service = _site_areas

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all SiteAreas from the DB
        tags:
            - SiteArea
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All SiteAreas
                schema:
                    type: array
                    items: SiteArea
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new SiteArea to the database
        tags:
            - SiteArea
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: SiteArea
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: SiteArea created successfully
                schema: SiteArea
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class SiteAreaPatchResource(Resource):
    _service = _site_areas

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one SiteArea from the DB
        tags:
            - SiteArea
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested SiteArea
                schema: SiteArea
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an SiteArea in the database
        tags:
            - SiteArea
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: SiteArea
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated SiteArea
                schema: SiteArea
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class SiteConstraintsPostResource(ListResource):
    _service = _site_constraints

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all SiteConstraintss from the DB
        tags:
            - SiteConstraints
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All SiteConstraintss
                schema:
                    type: array
                    items: SiteConstraints
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new SiteConstraints to the database
        tags:
            - SiteConstraints
        parameters:
            - in: body
              schema: SiteConstraints
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: SiteConstraints created successfully
                schema: SiteConstraints
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class SiteConstraintsPatchResource(Resource):
    _service = _site_constraints

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one SiteConstraints from the database
        tags:
            - SiteConstraints
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One SiteConstraints
                schema: SiteConstraints
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an SiteConstraints in the database
        tags:
            - SiteConstraints
        parameters:
            - in: body
              schema: SiteConstraints
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated SiteConstraints
                schema: SiteConstraints
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)
