from flask import session

from functools import wraps

def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        if 'logged_in' in session:
            return func(*args, **kargs)
        return 'You are NOT logged.'
    return wrapper
