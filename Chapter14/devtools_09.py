import time

def slowfunc(goslow=False):
    l = []
    for i in range(100):
        l.append(i)
        if goslow:
            time.sleep(0.01)
    return l


from cProfile import Profile

profiler = Profile()
profiler.runcall(slowfunc, True)
profiler.print_stats()

profiler = Profile()
profiler.runcall(slowfunc, False)
profiler.print_stats()