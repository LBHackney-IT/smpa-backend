import falcon

from typing import Optional

from ..schemas.core import CoreListSchema, CoreGetSchema  # NOQA
from .core import Resource, ListResource
from ..services.unit import _area_units, _linear_units


class AreaUnitListResource(ListResource):
    _service = _area_units
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all AreaUnits from the DB
        tags:
            - AreaUnit
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All AreaUnits
                schema:
                    type: array
                    items: AreaUnit
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)


class AreaUnitResource(Resource):
    _service = _area_units
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one AreaUnit from the DB
        tags:
            - AreaUnit
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested AreaUnit
                schema: AreaUnit
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an AreaUnit in the database
        tags:
            - AreaUnit
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: AreaUnit
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated AreaUnit
                schema: AreaUnit
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
        summary: Add new AreaUnit to the database
        tags:
            - AreaUnit
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: AreaUnit
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: AreaUnit created successfully
                schema: AreaUnit
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class LinearUnitListResource(ListResource):
    _service = _linear_units
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all LinearUnits from the DB
        tags:
            - LinearUnit
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All LinearUnits
                schema:
                    type: array
                    items: LinearUnit
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new LinearUnit to the database
        tags:
            - LinearUnit
        parameters:
            - in: body
              schema: LinearUnit
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: LinearUnit created successfully
                schema: LinearUnit
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class LinearUnitResource(Resource):
    _service = _linear_units
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one LinearUnit from the database
        tags:
            - LinearUnit
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One LinearUnit
                schema: LinearUnit
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an LinearUnit in the database
        tags:
            - LinearUnit
        parameters:
            - in: body
              schema: LinearUnit
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated LinearUnit
                schema: LinearUnit
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)
