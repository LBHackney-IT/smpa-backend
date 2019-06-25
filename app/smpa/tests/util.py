import json
import functools
from smpa.helpers.console import console


def purger(services):
    """A decorator for purging all objects in one or
    more services before and after a test.

    Args:
        services (RService or list): One or more services to purge
    """
    def decorator_purger(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal services
            if not isinstance(services, list):
                services = [services]
            for _service in services:
                console.info(_service)
                _service._purge()
            func(*args, **kwargs)
            for _service in services:
                _service._purge()
            return True
        return wrapper
    return decorator_purger


def json_match(result: dict, body: str) -> bool:
    """Test to see if the ``result`` from an API call contains all the
    data sent to it in ``body``

    Args:
        result (str): The API call result
        body (dict): The data we sent to the API
    """
    diffs = {}
    body_dict = json.loads(body)
    for k, v in body_dict.items():
        if result[k] != v:
            diffs[k] = {"wanted": v, "found": result[k]}

    if len(diffs):
        console.warn('JSON MATCH ERROR')
        console.warn(diffs)
        return False
    return True
