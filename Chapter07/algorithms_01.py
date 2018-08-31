import bisect

values = [ 5, 3, 1, 7 ]
print(5 in values)

sorted_values = sorted(values)
print(sorted_values)

def bisect_search(container, value):
    index = bisect.bisect_left(container, value)
    return index < len(container) and container[index] == value

print(bisect_search(sorted_values, 5))


import timeit
values = list(range(1000))

print(900 in values)
print(bisect_search(values, 900))

print(timeit.timeit(lambda: 900 in values))
print(timeit.timeit(lambda: bisect_search(values, 900)))
