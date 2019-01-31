import json
import falcon

from .core import Resource
from ..services.user import _users, _agents, _applicants


class UserResource(Resource):
    _service = _users


class AgentResource(Resource):
    _service = _agents


class ApplicantResource(Resource):
    _service = _applicants
