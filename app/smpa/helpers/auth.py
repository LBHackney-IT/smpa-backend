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
        resource = args[0]
        req = args[1]
        _service = resource._service
        user = req.context['user']
        # Always allow admins
        if user.is_admin:
            return f(*args, **kwargs)
        user.export()  # <- This loads our related data
        id = kwargs.get('id')
        obj = _service.get_or_404(id)
        if hasattr(obj, 'owner_id') and str(obj.owner_id) != str(user.id):
            raise falcon.HTTPError(falcon.HTTP_401, 'Error')
        return f(*args, **kwargs)
    return wrapper


def admin(f):
    """An authorisation decorator that ensures the user
    requesting the resource is an admin.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        req = args[1]
        user = req.context['user']
        if not user.is_admin:
            raise falcon.HTTPError(falcon.HTTP_401, 'Error')
        return f(*args, **kwargs)
    return wrapper


def admin_or_self(f):
    """Auth decorator specific to users to ensure the authenticated user is
    the user being operated on or an admin.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        req = args[1]
        user = req.context['user']
        id = kwargs.get('id')
        if str(id) != str(user.id) and not user.is_admin:
            raise falcon.HTTPError(falcon.HTTP_401, 'Error')
        return f(*args, **kwargs)
    return wrapper
