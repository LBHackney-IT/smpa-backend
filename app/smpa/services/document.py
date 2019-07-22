# -*- coding: utf-8 -*-

"""
    services.unit
    ~~~~~~~~~~~~~
    Services for units of measurement.
"""
import falcon
import uuid
import mimetypes
from .rethink import RService

from smpa.helpers.s3 import s3
from smpa.models.document import DocumentSize, DocumentFile


class DocumentSizeService(RService):
    __model__ = DocumentSize


_document_sizes = DocumentSizeService()


class DocumentFileService(RService):
    __model__ = DocumentFile

    def create(self, req, application_id):
        d = self.new()
        d.id = uuid.uuid4()
        d.application_id = application_id
        d.document_size_id = req.get_param('document_size_id')
        ext = mimetypes.guess_extension(req.content_type)
        path = f"{application_id}/{d.id}.{ext}"

        file_obj = req.get_param('body')
        uploaded = s3.save(file_obj, path)

        if not uploaded:
            raise falcon.HTTPError(falcon.HTTP_422)

        d.storage_path = path
        d.original_name = file_obj.filename
        _document_files.save(d)
        return d


_document_files = DocumentFileService()
