import json
import falcon

from typing import Optional

from .core import Resource
from ..services.user import _users, _agents, _applicants


class UserResource(Resource):
    _service = _users

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more Users from the database
        tags:
            - User
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more Users
                schema:
                    type: array
                    items: User
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update a User in the database
        tags:
            - User
        parameters:
            - in: body
              schema: User
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated User
                schema: User
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new User to the database
        tags:
            - User
        parameters:
            - in: body
              schema: User
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: User created successfully
                schema: User
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class AgentResource(Resource):
    _service = _agents

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more Agents from the database
        tags:
            - Agent
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more Agents
                schema:
                    type: array
                    items: Agent
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an Agent in the database
        tags:
            - Agent
        parameters:
            - in: body
              schema: Agent
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated Agent
                schema: Agent
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new Agent to the database
        tags:
            - Agent
        parameters:
            - in: body
              schema: Agent
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: Agent created successfully
                schema: Agent
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class ApplicantResource(Resource):
    _service = _applicants

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more Applicants from the database
        tags:
            - Applicant
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more Applicants
                schema:
                    type: array
                    items: Applicant
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an Applicant in the database
        tags:
            - Applicant
        parameters:
            - in: body
              schema: Applicant
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated Applicant
                schema: Applicant
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new Applicant to the database
        tags:
            - Applicant
        parameters:
            - in: body
              schema: Applicant
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: Applicant created successfully
                schema: Applicant
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)
