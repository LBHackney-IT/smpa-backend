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

from typing import Optional, List

from smpa.helpers.s3 import s3
from smpa.models.document import DocumentSize, DocumentFile, DocumentType


class DocumentSizeService(RService):
    __model__ = DocumentSize


_document_sizes = DocumentSizeService()


class DocumentTypeService(RService):
    __model__ = DocumentType


_document_types = DocumentTypeService()


class DocumentFileService(RService):
    __model__ = DocumentFile

    def create(self, req):
        d = self.new()
        d.id = uuid.uuid4()
        d.application_id = req.get_param('application_id')
        d.document_size_id = req.get_param('document_size_id')
        d.document_types_existing_ids = self._decode_str_list(req.get_param('existing'))
        d.document_types_proposed_ids = self._decode_str_list(req.get_param('proposed'))

        file_obj = req.get_param('document')
        ext = mimetypes.guess_extension(file_obj.type)
        if ext == '.jpe':
            ext = '.jpg'
        path = f"{d.application_id}/{d.id}{ext}"
        uploaded = s3.save(file_obj, path)

        if not uploaded:
            raise falcon.HTTPError(falcon.HTTP_422)

        d.storage_path = path
        d.original_name = str(file_obj.filename).split('/')[-1]
        _document_files.save(d)
        return d

    def _decode_str_list(self, value: Optional[str]) -> List[str]:
        """takes a str which is a comma separated list of ids and returns as
        a list of str ids.

        Args:
            value (Optional[str]): The string to decode.
        """
        if value is None or value == "":
            return []

        else:
            return value.strip().split(',')


_document_files = DocumentFileService()
