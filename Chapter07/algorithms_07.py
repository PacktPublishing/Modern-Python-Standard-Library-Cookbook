values = [ 1, 2, 3, 4, 5 ]

import functools, operator
print(
    functools.reduce(operator.add, values)
)

import itertools
print(
    list(itertools.accumulate(values, operator.add))
)
