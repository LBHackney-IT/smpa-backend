import falcon
import simplejson as json

from ..schemas.auth import login_schema
from ..services.user import _users


class AuthResource:
    auth = {"auth_disabled": True}
    deserializers = {"post": login_schema}

    def on_post(self, req: falcon.Request, resp: falcon.Response):
        """
        ---
        summary: Login into user account and generate JWT
        tags:
            - Login
        parameters:
            - in: body
              schema: LoginSchema
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Login Successful
                schema:
                    type: object
                    properties:
                        message:
                            type: string
                        jwt:
                            type: string
            401:
                description: Login Unsuccessful
            422:
                description: Input body formatting issue
        """
        from ..app import auth_backend
        user = _users.authenticate(req._params)
        jwt_token = auth_backend.get_auth_token({"id": str(user.id)})

        resp.status = falcon.HTTP_OK
        resp.media = {
            "message": "login successful!",
            "jwt": jwt_token,
            "user": user.export()
        }


class SignupResource:
    auth = {"auth_disabled": True}
    deserializers = {"post": login_schema}

    def on_post(self, req: falcon.Request, resp: falcon.Response):
        """
        ---
        summary: Create a user account
        tags:
            - Signup
        parameters:
            - in: body
              schema: LoginSchema
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: Signup Successful
                schema:
                    type: object
                    properties:
                        message:
                            type: string
            401:
                description: Signup Unsuccessful
            422:
                description: Input body formatting issue
        """
        email = req.get_param('email')
        password = req.get_param('password')
        password_confirm = req.get_param('password_confirm')
        resp.status = falcon.HTTP_401
        if password_confirm != password:
            rv = {
                'success': False,
                'message': 'Passwords do not match'
            }
        elif len(password) < 8:
            rv = {
                'success': False,
                'message': 'Passwords must be at least 8 characters'
            }
        elif _users.first(email=email) is not None:
            rv = {
                'success': False,
                'message': 'Email is already registered'
            }
        else:
            rv = _users.register(email, password)
            resp.status = falcon.HTTP_201

        resp.body = rv
