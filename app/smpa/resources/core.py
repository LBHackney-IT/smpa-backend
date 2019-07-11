import json

import falcon
from marshmallow import MarshalResult
from typing import List, Union

from ..helpers.console import console


class Resource(object):
    """Base Resource class for making stuff extensible."""

    auth = {
        'exempt_methods': ['OPTIONS']
    }

    # def on_options(self, req, resp):
    #     resp.set_header('Access-Control-Allow-Headers', 'Content-Type')

    def _json_or_404(self, data: Union[MarshalResult, List[MarshalResult]]) -> str:
        """Take a MarshalResult object or list of MarshalResult objects
        and return the json.

        Args:
            data (Union[MarshalResult, List[MarshalResult]]): The data from the service class

        Returns:
            dict: JSON representation of the thing

        Raises:
            falcon.HTTPError: Description
        """
        if data is None:
            raise falcon.HTTPError(falcon.HTTP_404, 'Object not found')

        if isinstance(data, list):
            try:
                r = [_.export() for _ in data]
                j = json.dumps(r)
            except Exception as e:
                raise falcon.HTTPError(falcon.HTTP_400, 'Error', e)
        else:
            try:
                j = json.dumps(data.export())
            except Exception as e:
                raise falcon.HTTPError(falcon.HTTP_400, 'Error', e)

        return j

    def _set_owner(self, req, instance):
        user = req.context['user']
        if hasattr(instance, 'owner_id') and instance.owner_id is None:
            instance.owner_id = str(user.id)
            self._service.save(instance)

    def on_get(self, req, resp, id=None):
        """Handles GET requests.

        If passed an ID, it should return a single existing record,
        otherwise return them all.

        Args:
            req (falcon.request.Request): A request
            resp (falcon.response.Response): A response
            id (str, optional): A resource ID
        """
        if id:
            rv = self._service.get(id)
            resp.body = self._json_or_404(rv)
            req.context.id = id
            req.context.obj = rv
        else:
            rv = self._service.all()
            resp.body = self._json_or_404(rv)

    def on_patch(self, req, resp, id=None):
        """Handles PATCH requests.

        Updates an existing resource.

        Args:
            req (falcon.request.Request): A request
            resp (falcon.response.Response): A response
            id (str): A resource ID

        Raises:
            falcon.HTTPError: Description
        """

        try:
            raw_json = req.stream.read()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', e.message)

        try:
            result = json.loads(raw_json, encoding='utf-8')
            rv = self._service.update(id, json=result)

            if not isinstance(rv, list):
                resp.body = self._json_or_404(rv)
            else:
                resp.body = self._json_or_404([_ for _ in rv])

        except ValueError:
            raise falcon.HTTPError(
                falcon.HTTP_422,
                'Invalid JSON',
                'Could not decode the request body. The JSON was incorrect.'
            )

    def on_post(self, req, resp):
        """Handles POST requests.

        Creates a new object in the db

        Args:
            req (falcon.request.Request): A request
            resp (falcon.response.Response): A response

        Raises:
            falcon.HTTPError: Description
        """

        try:
            raw_json = req.stream.read()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', e.message)

        try:
            result = json.loads(raw_json, encoding='utf-8')
            console.info(result)
            rv = self._service.create(json=result)
            self._set_owner(req, rv)

            if not isinstance(rv, list):
                resp.body = self._json_or_404(rv)
            else:
                resp.body = self._json_or_404([_ for _ in rv])

        except ValueError:
            raise falcon.HTTPError(
                falcon.HTTP_422,
                'Invalid JSON',
                'Could not decode the request body. The JSON was incorrect.'
            )


class ListResource(Resource):
    """Base Resource class for making stuff extensible."""

    def on_get(self, req, resp):
        """Handles GET requests.

        Returns multiple objects.

        Args:
            req (falcon.request.Request): A request
            resp (falcon.response.Response): A response
        """
        rv = self._service.all()
        resp.body = self._json_or_404(rv)
