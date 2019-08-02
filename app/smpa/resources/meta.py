import falcon

from ..schemas.core import CoreListSchema, CoreGetSchema  # NOQA
from .core import ListResource
from ..services.meta import _declarations


class DeclarationListResource(ListResource):
    _service = _declarations
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all Declarations from the DB
        tags:
            - Declaration
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All Declarations
                schema:
                    type: array
                    items: Declaration
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)


class OwnershipTypeListResource(ListResource):
    _service = _declarations
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all OwnershipTypes from the DB
        tags:
            - OwnershipType
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All OwnershipTypes
                schema:
                    type: array
                    items: OwnershipType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)
