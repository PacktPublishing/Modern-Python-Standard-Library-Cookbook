from functools import wraps


def decorator(f):
    @wraps(f)
    def _f(*args, **kwargs):
        return f(*args, **kwargs)
    return _f


@decorator
def sumthree(a, b):
    """Sums a and b"""
    return a + back


print(sumthree.__name__)

print(sumthree.__doc__)
