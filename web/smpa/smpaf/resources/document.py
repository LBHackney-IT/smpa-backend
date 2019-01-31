import falcon

from .core import Resource
from ..services.document import _document_sizes


class DocumentSizeResource(Resource):
    _service = _document_sizes
