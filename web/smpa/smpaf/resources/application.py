import json
import falcon

from typing import Optional

from .core import Resource, ListResource
from ..services.application import _applications


class ApplicationListResource(ListResource):
    _service = _applications

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all Applications from the DB
        tags:
            - Application
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All Applications
                schema:
                    type: array
                    items: Application
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)


class ApplicationResource(Resource):
    _service = _applications

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one Application from the DB
        tags:
            - Application
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested Application
                schema: Application
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an Application in the database
        tags:
            - Application
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: Application
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated Application
                schema: Application
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
        summary: Add new Application to the database
        tags:
            - Application
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: Application
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: Application created successfully
                schema: Application
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)
