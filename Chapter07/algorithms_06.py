import itertools
c = itertools.product(('A', 'B', 'C'), repeat=2)

print(
    list(c)
)

c = itertools.permutations(('A', 'B', 'C'), 2)
print(
    list(c)
)

c = itertools.combinations(('A', 'B', 'C'), 2)
print(
    list(c)
)
