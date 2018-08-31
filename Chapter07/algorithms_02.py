import itertools

def iter_nth(iterable, nth):
    return next(itertools.islice(iterable, nth, nth+1))

values = (x for x in range(10))
print(iter_nth(values, 4))
