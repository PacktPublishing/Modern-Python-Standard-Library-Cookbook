import os

def fib(n, seen):
    if n not in seen and n % 5 == 0:
        # Print out only numbers we didn't yet compute
        print(os.getpid(), '->', n)
        seen.add(n)

    if n < 2:
        return n
    return fib(n-2, seen) + fib(n-1, seen)

from multiprocessing import Pool
pool = Pool()
t1 = pool.apply_async(fib, args=(20, set()))
t2 = pool.apply_async(fib, args=(22, set()))
pool.close()
pool.join()
print(
    t1.get()
)
print(
    t2.get()
)
