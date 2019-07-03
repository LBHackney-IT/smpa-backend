import falcon
from functools import wraps
from smpa.helpers.console import console


def authorise(*args):
    roles = args



def owner(f):
    """An authorisation decorator that ensures the user
    requesting the resource is either the owner or an admin.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        authed = False
        resource = args[0]
        req = args[1]
        _service = resource._service
        user = req.context['user']
        user.export()  # <- This loads our related data
        if not authed:
            raise falcon.HTTPError(falcon.HTTP_403, 'Error')
        return f(*args, **kwargs)
    return wrapper


def admin(f):
    """An authorisation decorator that ensures the user
    requesting the resource is an admin.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        import ipdb; ipdb.set_trace()
        req = args[1]
        user = req.context['user']
        user.export()  # <- This loads our related data
        if not user.role.name != 'Admin' and user.role.name != 'SuperAdmin':
            raise falcon.HTTPError(falcon.HTTP_403, 'Error')
        return f(*args, **kwargs)
    return wrapper
