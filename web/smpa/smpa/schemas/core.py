from marshmallow import Schema, fields


class CoreGetSchema(Schema):
    id = fields.UUID()

    class Meta:
        strict = True


class CoreListSchema(Schema):
    page = fields.Int(missing=1)
    per_page = fields.Int(missing=20)

    class Meta:
        strict = True
