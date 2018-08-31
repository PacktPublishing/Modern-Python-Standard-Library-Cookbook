import contextlib

@contextlib.contextmanager
def logentrance():
    print('Enter')
    yield
    print('Exit')


with logentrance():
   print('This is inside')


@contextlib.contextmanager
def logentrance():
    print('Enter')
    try:
        yield
    except:
        print('Exception')
        raise
    finally:
        print('Exit')


with logentrance():
    raise Exception('This is an error')

