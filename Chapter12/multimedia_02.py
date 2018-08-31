import imghdr


def detect_image_format(filename):
    return imghdr.what(filename)


if __name__ == '__main__':
    import sys
    print(detect_image_format(sys.argv[1]))
    print(detect_image_format(open(sys.argv[1], 'rb')))