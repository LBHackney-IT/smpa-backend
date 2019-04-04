import falcon

from typing import Optional

from ..schemas.core import CoreListSchema, CoreGetSchema  # NOQA
from .core import Resource, ListResource
from ..services.work import _works_locations, _basement_works_types


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


class BasementWorksTypePost(ListResource):
    _service = _basement_works_types
    auth = {
        'exempt_methods': ['GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all BasementWorksTypes from the DB
        tags:
            - BasementWorksType
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All BasementWorksTypes
                schema:
                    type: array
                    items: BasementWorksType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)


class BasementWorksTypePatch(Resource):
    _service = _basement_works_types
    auth = {
        'exempt_methods': ['GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one BasementWorksType from the database
        tags:
            - BasementWorksType
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One BasementWorksType
                schema: BasementWorksType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an BasementWorksType in the database
        tags:
            - BasementWorksType
        parameters:
            - in: body
              schema: BasementWorksType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated BasementWorksType
                schema: BasementWorksType
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
        summary: Add new BasementWorksType to the database
        tags:
            - BasementWorksType
        parameters:
            - in: body
              schema: BasementWorksType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: BasementWorksType created successfully
                schema: BasementWorksType
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)
