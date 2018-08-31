import itertools

def group_by_key(iterable, key):
    iterable = sorted(iterable, key=key)
    return {k: list(g) for k,g in itertools.groupby(iterable, key)}

names = [('Alex', 'Zanardi'),
         ('Julius', 'Caesar'),
         ('Anakin', 'Skywalker'),
         ('Joseph', 'Joestar')]

print(
    group_by_key(names, lambda v: v[0][0])
)
