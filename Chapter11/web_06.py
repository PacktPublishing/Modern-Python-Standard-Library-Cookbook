import re
import inspect
from wsgiref.headers import Headers
from wsgiref.simple_server import make_server
from wsgiref.util import request_uri
from urllib.parse import parse_qs

class Response:
    def __init__(self):
        self.status = '200 OK'
        self.headers = Headers([
            ('Content-Type', 'text/html; charset=utf-8')
        ])

    def send(self, start_response):
        start_response(self.status, self.headers.items())


class Request:
    def __init__(self, environ):
        self.environ = environ
        self.urlargs = {}

    @property
    def path(self):
        return self.environ['PATH_INFO']

    @property
    def query(self):
        return parse_qs(self.environ['QUERY_STRING'])


class WSGIApplication:
    def __init__(self):
        self.routes = []

    def route(self, path):
        def _route_decorator(f):
            self.routes.append((re.compile(path), f))
            return f
        return _route_decorator

    def serve(self):
        httpd = make_server('', 8000, self)
        print("Serving on port 8000...")
        httpd.serve_forever()

    def _not_found(self, environ, resp):
        resp.status = '404 Not Found'
        return b"""<h1>Not Found</h1>"""

    def __call__(self, environ, start_response):
        request = Request(environ)

        routed_action = self._not_found
        for regex, action in self.routes:
            match = regex.fullmatch(request.path)
            if match:
                routed_action = action
                request.urlargs = match.groupdict()
                break

        resp = Response()

        if inspect.isclass(routed_action):
            routed_action = routed_action()
        body = routed_action(request, resp)

        resp.send(start_response)
        return [body]

    
app = WSGIApplication()

@app.route('/')
def index(request, resp):
    return b'Hello World, <a href="/link">Click here</a>'

@app.route('/link')
def link(request, resp):
    return (b'You clicked the link! '
            b'Try <a href="/args?a=1&b=2">Some arguments</a>')

@app.route('/args')
def args(request, resp):
    return (b'You provided %b<br/>'
            b'Try <a href="/name/HelloWorld">URL Arguments</a>' % 
            repr(request.query).encode('utf-8'))

@app.route('/name/(?P<first_name>\\w+)')
def name(request, resp):
    return (b'Your name: %b' % request.urlargs['first_name'].encode('utf-8'))

if __name__ == '__main__':
    app.serve()