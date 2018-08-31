import os.path
import socketserver
from http.server import SimpleHTTPRequestHandler, HTTPServer

class HTTPDirectoryRequestHandler(SimpleHTTPRequestHandler):
    SERVED_DIRECTORY = '.'

    def translate_path(self, path):
        path = super().translate_path(path)
        relpath = os.path.relpath(path)
        return os.path.join(self.SERVED_DIRECTORY, relpath)


class ThreadedHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    pass


def serve_directory(path, port=8001):
    class ConfiguredHandler(HTTPDirectoryRequestHandler):
        SERVED_DIRECTORY = path
    httpd = ThreadedHTTPServer(("", port), ConfiguredHandler)
    print("serving on port", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

serve_directory('/tmp')