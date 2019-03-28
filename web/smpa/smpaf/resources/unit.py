import json
import falcon

from typing import Optional

from .core import Resource
from ..services.unit import _area_units, _linear_units


class AreaUnitResource(Resource):
    _service = _area_units
    auth = {
        'exempt_methods': ['GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more AreaUnits from the database
        tags:
            - AreaUnit
        parameters:
            - in: id
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more AreaUnits
                schema:
                    type: array
                    items: AreaUnit
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
            - in: json
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
            - in: json
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


class LinearUnitResource(Resource):
    _service = _linear_units
    auth = {
        'exempt_methods': ['GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more LinearUnits from the database
        tags:
            - LinearUnit
        parameters:
            - in: id
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more LinearUnits
                schema:
                    type: array
                    items: LinearUnit
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
            - in: json
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

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new LinearUnit to the database
        tags:
            - LinearUnit
        parameters:
            - in: json
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
