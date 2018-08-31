import imghdr
import struct
import os
from pathlib import Path


class ImageReader:
    @classmethod
    def get_size(cls, f):    
        requires_close = False
        if isinstance(f, (str, getattr(os, 'PathLike', str))):
            f = open(f, 'rb')
            requires_close = True
        elif isinstance(f, Path):
            f = f.expanduser().open('rb')
            requires_close = True
        
        try:
            image_type = imghdr.what(f)
            if image_type not in ('jpeg', 'png', 'gif'):
                raise ValueError('Unsupported image format')

            f.seek(0)
            size_reader = getattr(cls, '_size_{}'.format(image_type))
            return size_reader(f)
        finally:
            if requires_close: f.close()

    @classmethod
    def _size_gif(cls, f):
        f.read(6)  # Skip the Magick Numbers
        w, h = struct.unpack('<HH', f.read(4))
        return w, h

    @classmethod
    def _size_png(cls, f):
        f.read(8)  # Skip Magic Number
        clen, ctype = struct.unpack('>I4s', f.read(8))
        if ctype != b'IHDR':
            raise ValueError('Unsupported PNG format')
        w, h = struct.unpack('>II', f.read(8))
        return w, h

    @classmethod
    def _size_jpeg(cls, f):
        start_of_image = f.read(2)
        if start_of_image != b'\xff\xd8':
            raise ValueError('Unsupported JPEG format')
        while True:
            marker, segment_size = struct.unpack('>2sH', f.read(4))
            if marker[0] != 0xff:
                raise ValueError('Unsupported JPEG format')
            data = f.read(segment_size - 2)
            if not 0xc0 <= marker[1] <= 0xcf:
                continue
            _, h, w = struct.unpack('>cHH', data[:5])
            break
        return w, h


if __name__ == '__main__':
    import sys
    print(
        ImageReader.get_size(sys.argv[1])
    )
    print(
        ImageReader.get_size(open(sys.argv[1], 'rb'))
    )
    print(
        ImageReader.get_size(Path(sys.argv[1]))
    )