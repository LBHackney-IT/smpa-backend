import json
import falcon


class Resource(object):
    """Base Resource class for making stuff extensible."""

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
            resp.body = json.dumps(rv.to_primitive())
        else:
            rv = self._service.all()
            resp.body = json.dumps([_.to_primitive() for _ in rv])

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
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,'Error',ex.message)

        try:
            result = json.loads(raw_json, encoding='utf-8')
            if id is None:
                rv = self._service.create(result)
            else:
                rv = self._service.update(id, result)

            if not isinstance(rv, list):
                resp.body = json.dumps(rv.to_primitive())
            else:
                resp.body = json.dumps([_.to_primitive() for _ in rv])

        except ValueError:
            raise falcon.HTTPError(
                falcon.HTTP_400,
                'Invalid JSON',
                'Could not decode the request body. The JSON was incorrect.'
            )
