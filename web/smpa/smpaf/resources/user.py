import json
import falcon

from .core import Resource
from ..services.user import _users, _agents, _applicants


class AuthResource(object):

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


class UserResource(Resource):
    _service = _users


class AgentResource(Resource):
    _service = _agents


class ApplicantResource(Resource):
    _service = _applicants
