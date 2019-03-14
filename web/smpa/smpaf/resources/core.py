import json
import falcon

from ..helpers.console import console


class Resource(object):
    """Base Resource class for making stuff extensible."""

    def _json_or_404(self, data):
        if data is None:
            raise falcon.HTTPError(falcon.HTTP_404, 'Object not found')

        if isinstance(data, list):
            try:
                j = json.dumps([_.to_primitive() for _ in data])
            except Exception as e:
                raise falcon.HTTPError(falcon.HTTP_400, 'Error', e.message)
        else:
            try:
                j = json.dumps(data.to_primitive())
            except Exception as e:
                raise falcon.HTTPError(falcon.HTTP_400, 'Error', e.message)

        return j

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
        else:
            rv = self._service.all()
            resp.body = self._json_or_404(rv)

    def on_post(self, req, resp, id=None):
        """Handles POST requests.

        If passed an ID, it should update an existing record, otherwise
        it should create a new one.

        Args:
            req (falcon.request.Request): A request
            resp (falcon.response.Response): A response
            id (str, optional): A resource ID

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
            if id is None:
                rv = self._service.create(json=result)
            else:
                rv = self._service.update(id, json=result)

            if not isinstance(rv, list):
                resp.body = self._json_or_404(rv)
            else:
                resp.body = self._json_or_404([_ for _ in rv])

        except ValueError:
            raise falcon.HTTPError(
                falcon.HTTP_400,
                'Invalid JSON',
                'Could not decode the request body. The JSON was incorrect.'
            )
