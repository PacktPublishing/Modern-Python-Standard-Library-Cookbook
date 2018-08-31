import tempfile

with tempfile.SpooledTemporaryFile(max_size=30) as temp:
    for i in range(3):
        temp.write(b'Line of text\n')

    temp.seek(0)
    print(temp.read())
