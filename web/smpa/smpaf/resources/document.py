import falcon

from .core import Resource
from ..services.document import _document_sizes


class DocumentSizeResource(Resource):
    _service = _document_sizes
    auth = {
        'exempt_methods': ['GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more DocumentSizes from the database
        tags:
            - DocumentSize
        parameters:
            - in: id
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more DocumentSizes
                schema:
                    type: array
                    items: DocumentSize
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update a DocumentSize in the database
        tags:
            - DocumentSize
        parameters:
            - in: json
              schema: DocumentSize
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated DocumentSize
                schema: DocumentSize
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
        summary: Add new DocumentSize to the database
        tags:
            - DocumentSize
        parameters:
            - in: json
              schema: DocumentSize
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: DocumentSize created successfully
                schema: DocumentSize
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)
