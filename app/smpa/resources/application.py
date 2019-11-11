import json
import falcon

from typing import Optional

from smpa.helpers.auth import owner, admin
from .core import Resource, ListResource
from ..services.application import _applications, _application_statuses


class ApplicationSubmittedList(ListResource):
    _service = _applications

    @admin
    def on_get(
            self, req: falcon.Request, resp: falcon.Response, since: Optional[str] = None) -> None:
        """
        For an admin user, this endpoint returns all applications, for a user it
        returns all of the applications they own.
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
                description: All submitted Applications
                schema:
                    type: array
                    items: Application
            401:
                description: Unauthorized
        """
        rv = self._service.submitted(since=since)
        resp.body = self._json_or_404(rv)


class ApplicationSubmitResource(Resource):
    _service = _applications

    @owner
    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None):
        """
        {
            "submitted": true
        }
        ---
        summary: Submit an application to the planning department. This endpoint should only ever
        receive "submitted": true

        tags:
            - Application
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The Application
                schema: Application
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        if req.media != {'submitted': True}:
            raise falcon.HTTPError(falcon.HTTP_422, "Incorrect input")
        else:
            application = self._service.get(id)
            if application.submitted_at is not None:
                raise falcon.HTTPError(falcon.HTTP_422, "Application is already submitted")

        application = self._service.submit(str(id))
        resp.status = falcon.HTTP_200
        resp.body = self._json_or_404(application)


class ApplicationStatusListResource(ListResource):
    _service = _application_statuses

    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all ApplicationStatuses from the DB
        tags:
            - ApplicationStatus
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All ApplicationStatuses
                schema:
                    type: array
                    items: ApplicationStatus
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)


class ApplicationResourcePost(ListResource):
    _service = _applications

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        For an admin user, this endpoint returns all applications, for a user it
        returns all of the applications they own.
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
        user = req.context['user']
        user.export()
        if not user.is_admin:
            rv = self._service.find(owner_id=str(user.id))
            resp.body = self._json_or_404(rv)
        else:
            rv = self._service.all()
            resp.body = self._json_or_404(rv)

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


class ApplicationResourcePatch(Resource):
    _service = _applications

    @owner
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

    @owner
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
