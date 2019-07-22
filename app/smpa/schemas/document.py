from marshmallow import fields, Schema


class DocumentUploadSchema(Schema):
    document_size_id = fields.Str(required=True)


document_upload_schema = DocumentUploadSchema()
