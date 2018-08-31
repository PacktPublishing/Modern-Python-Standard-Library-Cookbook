import sys

def decode_filename(fname):
    fse = sys.getfilesystemencoding()
    return fname.decode(fse, "surrogateescape")