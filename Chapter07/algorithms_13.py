from contextlib import ExitStack
import contextlib

@contextlib.contextmanager
def first():
    print('First')
    yield

@contextlib.contextmanager
def second():
    print('Second')
    yield

for n in range(5):
    with ExitStack() as stack:
        stack.enter_context(first())
        if n % 2 == 0:
            stack.enter_context(second())
        print('NUMBER: {}'.format(n))
