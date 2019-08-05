import falcon

from typing import Optional

from smpa.schemas.core import CoreListSchema, CoreGetSchema  # NOQA
from smpa.helpers.auth import owner
from smpa.services.payment import _payments

from .core import Resource, ListResource


class PaymentPostResource(ListResource):
    _service = _payments

    def on_post(self, req: falcon.Request, resp: falcon.Response, id: str):
        """
        ---
        summary: Add new Payment to the database and upload a file
        tags:
            - Payment
        parameters:
            - in: body
              schema: Payment
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: Payment created successfully
                schema: Payment
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        application_id = id
        rv = _payments.create(req, application_id)

        resp.status = falcon.HTTP_201
        resp.body = self._json_or_404(rv)

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all payments owned by the authenticated user from the DB or all if admin
        tags:
            - Payment
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All Payments
                schema:
                    type: array
                    items: Payment
            401:
                description: Unauthorized
        """
        user = req.context['user']
        user.export()
        if 'Admin' not in user.role.name:
            rv = self._service.find(owner_id=str(user.id))
            resp.body = self._json_or_404(rv)
        else:
            rv = self._service.all()
            resp.body = self._json_or_404(rv)


class PaymentPatchResource(Resource):
    _service = _payments

    @owner
    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one Payment from the DB
        tags:
            - Payment
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested Payment
                schema: Payment
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    @owner
    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an Payment in the database
        tags:
            - Payment
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: Payment
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated Payment
                schema: Payment
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)
