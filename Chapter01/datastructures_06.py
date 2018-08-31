import time
import heapq

class PriorityQueue(object):
    def __init__(self):
        self._q = []

    def add(self, value, priority=0):
        heapq.heappush(self._q, (priority, time.time(), value))

    def pop(self):
        return heapq.heappop(self._q)[-1]


def f1(): print('hello')
def f2(): print('world')

pq = PriorityQueue()
pq.add(f2, priority=1)
pq.add(f1, priority=0)
pq.pop()()
pq.pop()()
