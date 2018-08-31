import time
from http.cookies import SimpleCookie

from web_06 import WSGIApplication

app = WSGIApplication()

@app.route('/')
def index(req, resp):
    if 'HTTP_COOKIE' in req.environ:
        cookies = SimpleCookie(req.environ['HTTP_COOKIE'])
        if 'identity' in cookies:
            return b'Welcome back, %b' % cookies['identity'].value.encode('utf-8')
    return b'Visit <a href="/identity">/identity</a> to get an identity'


@app.route('/identity')
def identity(req, resp):
    identity = int(time.time())

    cookie = SimpleCookie()
    cookie['identity'] = 'USER: {}'.format(identity)
    
    for set_cookie in cookie.values():
        resp.headers.add_header('Set-Cookie', set_cookie.OutputString())
    return b'Go back to <a href="/">index</a> to check your identity'


app.serve()