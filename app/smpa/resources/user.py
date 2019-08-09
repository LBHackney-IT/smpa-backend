import uuid
import arrow
import falcon

from typing import Optional
from smpa.helpers.auth import owner, admin, admin_or_self  # NOQA

from .core import Resource, ListResource
from ..schemas.auth import login_schema
from ..services.user import _users, _agents, _applicants, _user_profiles


class UserResourcePatch(Resource):
    _service = _users

    @admin_or_self
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
                description: Get one user
                schema:
                    type: array
                    items: User
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    @admin_or_self
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


class UserResourceList(ListResource):
    _service = _users

    @admin
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all Users from the DB
        tags:
            - User
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All Users
                schema:
                    type: array
                    items: User
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)


class UserResourcePost(Resource):
    _service = _users

    auth = {"auth_disabled": True}
    deserializers = {"post": login_schema}

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
        email = req.get_param('email')
        password = req.get_param('password')
        password_confirm = req.get_param('password_confirm')
        self._service.verify_passwords(password, password_confirm)
        if _users.first(email=email) is not None:
            resp.status = falcon.HTTP_401
            resp.media = {
                'success': False,
                'message': 'Email is already registered'
            }
        else:
            user = _users.register(email, password)
            rv = self._json_or_404(user)
            resp.status = falcon.HTTP_201
            resp.body = rv


class PasswordResetResource(Resource):
    _service = _users

    auth = {"auth_disabled": True}

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Reset a user's password
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
                description: Password reset success
                schema: User
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        from smpa.app import config, govnotify
        if 'email' in req.media:
            email = req.media.get('email')
            user = self._validate_reset(email)
            # This is step 1. We set a reset token against the user
            # and then send an email with their reset link.
            token = uuid.uuid4()
            user.reset_token = str(token)
            user.reset_token_expires = arrow.now().shift(hours=24)
            user = self._service.save(user)
            reset_link = config.get_password_reset_url(token)
            govnotify.send_password_reset(email, reset_link)
            resp.status = falcon.HTTP_OK
            resp.media = {
                'success': True,
                'message': "Password reset initiated"
            }
        elif 'token' in req.media:
            token = req.media.get('token')
            password = req.media.get('password')
            password_confirm = req.media.get('password_confirm')
            user = self._validate_token(token, password, password_confirm)
            self._service.verify_passwords(password, password_confirm)
            user = self._service.set_password(user, password)
            user.reset_token = None
            user.reset_token_expires = None
            _users.save(user)
            resp.status = falcon.HTTP_OK
            resp.media = {
                'success': True,
                'message': "Password reset successful"
            }
        else:
            raise falcon.HTTPError(falcon.HTTP_422, "Unable to process request")

    def _validate_reset(self, email: str):
        """Run some checks and return a user if they pass

        Args:
            email (str): The email address we're validating

        Raises:
            falcon.HTTPError: Various errors
        """
        if not isinstance(email, str):
            raise falcon.HTTPError(falcon.HTTP_422, 'Invalid input')
        user = self._service.first_or_404(email=email)
        return user

    def _validate_token(self, token: str, password: str, password_confirm: str):
        """Run some checks and return a user if they pass

        Args:
            token (str): The token we're validating

        Raises:
            falcon.HTTPError: Various errors
        """
        if not isinstance(token, str):
            raise falcon.HTTPError(falcon.HTTP_422, 'Invalid input')
        user = self._service.first_or_404(reset_token=token)
        if arrow.get(user.reset_token_expires) < arrow.now():
            raise falcon.HTTPError(falcon.HTTP_400, 'Reset token has expired')
        self._service.verify_passwords(password, password_confirm)

        return user


class UserVerifyResource(Resource):
    _service = _users

    auth = {"auth_disabled": True}

    def on_get(self, req: falcon.Request, resp: falcon.Response, token: str):
        """
        Args:
            req (falcon.Request): Description
            resp (falcon.Response): Description
            token (str): Description
        ---
        summary: Verify a user's account and log them in
        tags:
            - User
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: User verified and logged in
                schema:
                    type: object
                    properties:
                        message:
                            type: string
                        jwt:
                            type: string
            401:
                description: Unauthorized
        """
        from ..app import auth_backend
        user = self._service.verify_account(token)
        jwt_token = auth_backend.get_auth_token({"id": str(user.id)})
        resp.status = falcon.HTTP_OK
        resp.media = {"message": "Account verified and logged in", "jwt": jwt_token}


class UserProfileResourcePatch(Resource):
    _service = _user_profiles

    @admin_or_self
    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more UserProfiles from the database
        tags:
            - UserProfile
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: Get one user
                schema:
                    type: array
                    items: UserProfile
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    @admin_or_self
    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update a UserProfile in the database
        tags:
            - UserProfile
        parameters:
            - in: body
              schema: UserProfile
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated UserProfile
                schema: UserProfile
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)

# We probably don't need this resource
# class UserProfileResourcePost(ListResource):
#     _service = _users

#     @admin
#     def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
#         """
#         ---
#         summary: Get all UserProfiles from the DB
#         tags:
#             - User
#         parameters:
#             - in: query
#               schema: CoreListSchema
#         produces:
#             - application/json
#         responses:
#             200:
#                 description: All UserProfiles
#                 schema:
#                     type: array
#                     items: User
#             401:
#                 description: Unauthorized
#         """
#         super().on_get(req, resp)

#     @admin
#     def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
#         """
#         ---
#         summary: Add new UserProfile to the database
#         tags:
#             - UserProfile
#         parameters:
#             - in: body
#               schema: UserProfile
#         consumes:
#             - application/json
#         produces:
#             - application/json
#         responses:
#             201:
#                 description: UserProfile created successfully
#                 schema: UserProfile
#             401:
#                 description: Unauthorized
#             422:
#                 description: Input body formatting issue
#         """
#         super().on_post(req, resp)


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
