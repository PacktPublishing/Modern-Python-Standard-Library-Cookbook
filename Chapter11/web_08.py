from web_06 import WSGIApplication
from wsgiref.simple_server import make_server
import cgitb
import sys

app = WSGIApplication()

@app.route('/crash')
def crash(req, resp):
    raise RuntimeError('This is a crash!')


class ErrorMiddleware:
    """Wrap a WSGI application to display errors in the browser"""
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        app_iter = None
        try:
            app_iter = self.app(environ, start_response)
            for item in app_iter:
                yield item
        except:
            try:
                start_response('500 INTERNAL SERVER ERROR', [
                    ('Content-Type', 'text/html; charset=utf-8'),
                    ('X-XSS-Protection', '0'),
                ])
            except Exception:
                # There has been output but an error occurred later on. 
                # In that situation we can do nothing fancy anymore, 
                # better log something into the error log and fallback.
                environ['wsgi.errors'].write(
                    'Debugging middleware caught exception in streamed '
                    'response after response headers were already sent.\n'
                )
            else:
                yield cgitb.html(sys.exc_info()).encode('utf-8')
        finally:
            if hasattr(app_iter, 'close'):
                app_iter.close()


httpd = make_server('', 8000, ErrorMiddleware(app))
print("Serving on port 8000...")
httpd.serve_forever()