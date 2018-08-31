import io
import mimetypes
import uuid


class MultiPartForm:
    def __init__(self):
        self.fields = {}
        self.files = []

    def __setitem__(self, name, value):
        self.fields[name] = value

    def add_file(self, field, filename, data, mimetype=None):
        if mimetype is None:
            mimetype = (mimetypes.guess_type(filename)[0] or
                        'application/octet-stream')
        self.files.append((field, filename, mimetype, data))

    def _generate_bytes(self, boundary):
        buffer = io.BytesIO()
        for field, value in self.fields.items():
            buffer.write(b'--' + boundary + b'\r\n')
            buffer.write('Content-Disposition: form-data; '
                         'name="{}"\r\n'.format(field).encode('utf-8'))
            buffer.write(b'\r\n')
            buffer.write(value.encode('utf-8'))
            buffer.write(b'\r\n')
        for field, filename, f_content_type, body in self.files:
            buffer.write(b'--' + boundary + b'\r\n')
            buffer.write('Content-Disposition: file; '
                         'name="{}"; filename="{}"\r\n'.format(
                             field, filename
                         ).encode('utf-8'))
            buffer.write('Content-Type: {}\r\n'.format(
                f_content_type
            ).encode('utf-8'))
            buffer.write(b'\r\n')
            buffer.write(body)
            buffer.write(b'\r\n')
        buffer.write(b'--' + boundary + b'--\r\n')
        return buffer.getvalue()

    def encode(self):
        boundary = uuid.uuid4().hex.encode('ascii')
        while boundary in self._generate_bytes(boundary=b'NOBOUNDARY'):
            boundary = uuid.uuid4().hex.encode('ascii')

        content_type = 'multipart/form-data; boundary={}'.format(
            boundary.decode('ascii')
        )
        return content_type, self._generate_bytes(boundary)


form = MultiPartForm()
form['name'] = 'value'
form.add_file('file1', 'somefile.txt', b'Some Content', 'text/plain')
content_type, form_body = form.encode()
print(content_type, form_body.decode('ascii'))



from web_03 import http_request
_, resp = http_request('https://httpbin.org/post', method='POST',
                       data=form_body, headers={'Content-Type': content_type})
print(resp)


