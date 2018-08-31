import functools, operator

values = range(10)
mul3 = functools.partial(operator.mul, 3)
print(
    list(map(mul3, values))
)
