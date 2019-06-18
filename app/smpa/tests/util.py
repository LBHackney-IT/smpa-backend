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
