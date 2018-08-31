import cgi

from web_06 import WSGIApplication
import base64

app = WSGIApplication()

@app.route('/')
def index(req, resp):
    return (
        b'<form action="/upload" method="post" enctype="multipart/form-data">'
        b'  <input type="file" name="uploadedfile"/>'
        b'  <input type="submit" value="Upload">'
        b'</form>'
    )

@app.route('/upload')
def upload(req, resp):
    form = cgi.FieldStorage(fp=req.environ['wsgi.input'], 
                            environ=req.environ)
    if 'uploadedfile' not in form:
        return b'Nothing uploaded'
    
    uploadedfile = form['uploadedfile']
    if uploadedfile.type.startswith('image'):
        # User uploaded an image, show it
        return b'<img src="data:%b;base64,%b"/>' % (
            uploadedfile.type.encode('ascii'),
            base64.b64encode(uploadedfile.file.read())
        )
    elif uploadedfile.type.startswith('text'):
        return uploadedfile.file.read()
    else:
        return b'You uploaded %b' % uploadedfile.filename.encode('utf-8')


app.serve()