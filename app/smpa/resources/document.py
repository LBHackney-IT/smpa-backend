import os
import falcon
import tempfile

from typing import Optional

from smpa.resources.core import Resource, ListResource
from smpa.services.document import _document_sizes, _document_files, _document_types
from smpa.schemas.document import document_upload_schema


class DocumentFilePostResource(Resource):

    _service = _document_files

    def on_post(self, req: falcon.Request, resp: falcon.Response):
        """
        ---
        summary: Add new DocumentFile to the database and upload a file
        tags:
            - DocumentFile
        parameters:
            - in: body
              schema: DocumentFile
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: DocumentFile created successfully
                schema: DocumentFile
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        rv = _document_files.create(req)

        resp.status = falcon.HTTP_201
        resp.body = self._json_or_404(rv)


class DocumentFileApplicationResource(ListResource):

    _service = _document_files

    def on_get(self, req: falcon.Request, resp: falcon.Response, application_id: Optional[str] = None) -> None:
        """
        ---
        summary: Get an application's documents from the database
        tags:
            - Address
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: All documents associated with an application
                schema:
                    type: array
                    items: Address
            401:
                description: Unauthorized
        """
        rv = self._service.find(application_id=application_id)
        resp.body = self._json_or_404(rv)


class DocumentSizeResource(Resource):
    _service = _document_sizes
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more DocumentSizes from the database
        tags:
            - DocumentSize
        parameters:
            - in: path
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
            - in: body
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
            - in: body
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


class DocumentTypePostResource(ListResource):
    _service = _document_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all DocumentTypes from the DB
        tags:
            - DocumentType
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All DocumentTypes
                schema:
                    type: array
                    items: DocumentType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)


class DocumentTypePatchResource(Resource):
    _service = _document_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: str = None) -> None:
        """
        ---
        summary: Get one DocumentType from the database
        tags:
            - DocumentType
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One DocumentType
                schema: DocumentType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)
