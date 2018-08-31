def function1():
    l = []
    for i in range(100):
        l.append(i)
    return l


def function2():
    return [i for i in range(100)]


import timeit

print(
    timeit.timeit(function1)
)
print(
    timeit.timeit(function2)
)