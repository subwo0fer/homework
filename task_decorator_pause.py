from time import sleep
from functools import wraps


def pause(ps):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(ps)
            return func(*args, **kwargs)
        return wrapper
    return decorator
