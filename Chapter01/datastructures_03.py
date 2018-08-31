from collections import ChainMap

def f(a, b, c, d):
    print(a, b, c, d)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
f(**ChainMap(d1, d2))
