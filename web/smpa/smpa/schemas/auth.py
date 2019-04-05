from marshmallow import fields, post_load, Schema

import falcon

from ..exceptions import HTTPError
from ..services.user import _users


class LoginSchema(Schema):
    # Fields
    email = fields.Email(required=True)
    password = fields.Str(required=True)

    # Loaders
    @post_load
    def make_user(self, data):
        user = _users.first(email=data["email"])
        valid = _users.verify(user, data["password"])
        if not user or not valid:
            raise HTTPError(
                falcon.HTTP_UNAUTHORIZED,
                errors={"message": "Invalid username / password"},
            )
        return user


login_schema = LoginSchema()
