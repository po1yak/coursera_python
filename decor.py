import json
import functools

def to_json(func):
    @functools.wraps(func)
    def jsoned(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return jsoned

