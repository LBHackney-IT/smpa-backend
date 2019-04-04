import falcon

from typing import Optional

from ..schemas.core import CoreListSchema, CoreGetSchema  # NOQA
from .core import Resource, ListResource
from ..services.work import _works_locations, _basement_works_locations


class WorksLocationPost(ListResource):
    _service = _works_locations
    auth = {
        'exempt_methods': ['GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all WorksLocations from the DB
        tags:
            - WorksLocation
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All WorksLocations
                schema:
                    type: array
                    items: WorksLocation
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)


class WorksLocationPatch(Resource):
    _service = _works_locations
    auth = {
        'exempt_methods': ['GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one WorksLocation from the DB
        tags:
            - WorksLocation
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested WorksLocation
                schema: WorksLocation
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an WorksLocation in the database
        tags:
            - WorksLocation
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: WorksLocation
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated WorksLocation
                schema: WorksLocation
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new WorksLocation to the database
        tags:
            - WorksLocation
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: WorksLocation
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: WorksLocation created successfully
                schema: WorksLocation
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class BasementWorksLocationPost(ListResource):
    _service = _basement_works_locations
    auth = {
        'exempt_methods': ['GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all BasementWorksLocations from the DB
        tags:
            - BasementWorksLocation
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All BasementWorksLocations
                schema:
                    type: array
                    items: BasementWorksLocation
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)


class BasementWorksLocationPatch(Resource):
    _service = _basement_works_locations
    auth = {
        'exempt_methods': ['GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one BasementWorksLocation from the database
        tags:
            - BasementWorksLocation
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One BasementWorksLocation
                schema: BasementWorksLocation
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an BasementWorksLocation in the database
        tags:
            - BasementWorksLocation
        parameters:
            - in: body
              schema: BasementWorksLocation
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated BasementWorksLocation
                schema: BasementWorksLocation
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new BasementWorksLocation to the database
        tags:
            - BasementWorksLocation
        parameters:
            - in: body
              schema: BasementWorksLocation
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: BasementWorksLocation created successfully
                schema: BasementWorksLocation
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)
