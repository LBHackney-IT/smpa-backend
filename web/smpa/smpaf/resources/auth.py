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
        resp.media = {"message": "login successful!", "jwt": jwt_token}


class AuthResourceOLD(object):

    auth = {
        'exempt_methods': ['POST']
    }

    def on_get(self):
        raise NotImplementedError

    def on_post(self, req, resp):
        data = req.params
        user = _users.first(email=data['email'])
        if user is None:
            raise falcon.HTTPError(falcon.HTTP_403, 'User not found')

        if _users.verify(user, data['password']):
            token = _users.gen_token(user)
            rv = {'token': token}
            return json.dumps(rv)
        else:
            raise falcon.HTTPError(falcon.HTTP_403, 'Password incorrect')
