import falcon


class ApiSpecResource:
    auth = {"auth_disabled": True}

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        from ..app import spec
        swagger_specification: dict = spec.to_dict()

        resp.status = falcon.HTTP_200
        resp.media = swagger_specification
