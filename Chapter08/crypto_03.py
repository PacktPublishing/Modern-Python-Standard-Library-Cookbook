import hashlib

def verify_file(filepath, expectedhash, hashtype='md5'):
    with open(filepath, 'rb') as f:
        try:
            filehash = getattr(hashlib, hashtype)()
        except AttributeError:
            raise ValueError(
                'Unsupported hashing type %s' % hashtype
            ) from None

        while True:
            data = f.read(4096)
            if not data:
                break
            filehash.update(data)

    return filehash.hexdigest() == expectedhash


verifies = verify_file(
    'wrapt-1.10.11.tar.gz',
    'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
    'sha256'
)
print(verifies)