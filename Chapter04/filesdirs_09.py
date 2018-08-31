import tempfile, os


class safe_open(object):
    def __init__(self, path, mode='w+b'):
        self._target = path
        self._mode = mode

    def __enter__(self):
        self._file = tempfile.NamedTemporaryFile(self._mode, delete=False)
        return self._file

    def __exit__(self, exc_type, exc_value, traceback):
        self._file.close()
        if exc_type is None:
            os.rename(self._file.name, self._target)
        else:
            os.unlink(self._file.name)


with safe_open('/tmp/myfile') as f:
    f.write(b'Hello World')
print(open('/tmp/myfile').read())

with open('/tmp/myfile', 'wb+') as f:
    f.write(b'Replace the hello world, ')
    raise Exception('but crash meanwhile!')
    f.write(b'expect to write some more')
print(open('/tmp/myfile').read())

with safe_open('/tmp/myfile') as f:
    f.write(b'Replace the hello world, ')
    raise Exception('but crash meanwhile!')
    f.write(b'expect to write some more')
print(open('/tmp/myfile').read())
