import mimetypes

def guess_file_type(filename):
    if not getattr(guess_file_type, 'initialised', False):
        mimetypes.init()
        guess_file_type.initialised = True
    file_type, encoding = mimetypes.guess_type(filename)
    return file_type



if __name__ == '__main__':
    print(
        guess_file_type('~/Pictures/5565_1680x1050.jpg')
    )
    print(
        guess_file_type('~/Pictures/5565_1680x1050.jpeg')
    )
    print(
        guess_file_type('~/Pictures/avatar.png')
    )
    print(
        guess_file_type('/tmp/unable_to_guess.blob')
    )
    print(
        guess_file_type('/this/does/not/exists.txt')
    )