import itertools

values = [['a', 'b', 'c'],
          [1, 2, 3],
          ['X', 'Y', 'Z']]

chained = itertools.chain.from_iterable(values)
print(
    list(chained)
)
