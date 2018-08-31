import threading
import sched
import functools


class BackgroundScheduler(threading.Thread):
    def __init__(self, start=True):
        self._scheduler = sched.scheduler()
        self._running = True
        super().__init__(daemon=True)
        if start:
            self.start()

    def run_at(self, time, action, args=None, kwargs=None):
        self._scheduler.enterabs(time, 0, action,
                                argument=args or tuple(),
                                kwargs=kwargs or {})

    def run_after(self, delay, action, args=None, kwargs=None):
        self._scheduler.enter(delay, 0, action,
                            argument=args or tuple(),
                            kwargs=kwargs or {})

    def run_every(self, seconds, action, args=None, kwargs=None):
        @functools.wraps(action)
        def _f(*args, **kwargs):
            try:
                action(*args, **kwargs)
            finally:
                self.run_after(seconds, _f, args=args, kwargs=kwargs)
        self.run_after(seconds, _f, args=args, kwargs=kwargs)

    def run(self):
        while self._running:
            delta = self._scheduler.run(blocking=False)
            if delta is None:
                delta = 0.5
            self._scheduler.delayfunc(min(delta, 0.5))

    def stop(self):
        self._running = False

import time
s = BackgroundScheduler()
s.run_every(2, lambda: print('Hello World'))
time.sleep(5)
s.stop()
s.join()