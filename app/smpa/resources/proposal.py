import falcon

from typing import Optional

from smpa.helpers.auth import owner
from ..schemas.core import CoreListSchema, CoreGetSchema  # NOQA
from .core import Resource, ListResource
from ..services.proposal import _proposals_extension, _proposals_equipment


class ProposalExtensionPostResource(ListResource):
    _service = _proposals_extension

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all ProposalExtensions from the DB
        tags:
            - ProposalExtension
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All ProposalExtensions
                schema:
                    type: array
                    items: ProposalExtension
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new ProposalExtension to the database
        tags:
            - ProposalExtension
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: ProposalExtension
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: ProposalExtension created successfully
                schema: ProposalExtension
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class ProposalExtensionPatchResource(Resource):
    _service = _proposals_extension

    @owner
    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one ProposalExtension from the DB
        tags:
            - ProposalExtension
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested ProposalExtension
                schema: ProposalExtension
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    @owner
    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an ProposalExtension in the database
        tags:
            - ProposalExtension
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: ProposalExtension
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated ProposalExtension
                schema: ProposalExtension
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class ProposalEquipmentPostResource(ListResource):
    _service = _proposals_equipment

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all ProposalEquipments from the DB
        tags:
            - ProposalEquipment
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All ProposalEquipments
                schema:
                    type: array
                    items: ProposalEquipment
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new ProposalEquipment to the database
        tags:
            - ProposalEquipment
        parameters:
            - in: body
              schema: ProposalEquipment
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: ProposalEquipment created successfully
                schema: ProposalEquipment
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class ProposalEquipmentPatchResource(Resource):
    _service = _proposals_equipment

    @owner
    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one ProposalEquipment from the database
        tags:
            - ProposalEquipment
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One ProposalEquipment
                schema: ProposalEquipment
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    @owner
    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an ProposalEquipment in the database
        tags:
            - ProposalEquipment
        parameters:
            - in: body
              schema: ProposalEquipment
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated ProposalEquipment
                schema: ProposalEquipment
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)
