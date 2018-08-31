from web_06 import WSGIApplication

app = WSGIApplication()



class RestController:
    def __call__(self, req, resp):
        method = req.environ['REQUEST_METHOD']
        action = getattr(self, method, self._not_found)
        return action(req, resp)

    def _not_found(self, environ, resp):
        resp.status = '404 Not Found'
        return b'{}'  # Provide an empty JSON document


import json


@app.route('/resources/?(?P<id>\\w*)')
class ResourcesRestController(RestController):
    RESOURCES = {}

    def GET(self, req, resp):
        resource_id = req.urlargs['id']
        if not resource_id:
            # Whole catalog requested
            return json.dumps(self.RESOURCES).encode('utf-8')
        
        if resource_id not in self.RESOURCES:
            return self._not_found(req, resp)

        return json.dumps(self.RESOURCES[resource_id]).encode('utf-8')

    def POST(self, req, resp):
        content_length = int(req.environ['CONTENT_LENGTH'])
        data = req.environ['wsgi.input'].read(content_length).decode('utf-8')

        resource = json.loads(data)
        resource['id'] = str(len(self.RESOURCES)+1)
        self.RESOURCES[resource['id']] = resource
        return json.dumps(resource).encode('utf-8')

    def DELETE(self, req, resp):
        resource_id = req.urlargs['id']
        if not resource_id:
            return self._not_found(req, resp)
        self.RESOURCES.pop(resource_id, None)

        req.status = '204 No Content'
        return b''


import threading
threading.Thread(target=app.serve, daemon=True).start()


from web_03 import http_request
_, resp = http_request('http://localhost:8000/resources', method='POST', 
                       data=json.dumps({'name': 'Mario',
                                        'surname': 'Mario'}).encode('utf-8'))
print('NEW RESOURCE: ', resp)

_, resp = http_request('http://localhost:8000/resources')
print('ALL RESOURCES: ', resp)

http_request('http://localhost:8000/resources', method='POST', 
             data=json.dumps({'name': 'Luigi',
                              'surname': 'Mario'}).encode('utf-8'))
_, resp = http_request('http://localhost:8000/resources')
print('ALL RESOURCES: ', resp)

_, resp = http_request('http://localhost:8000/resources/1')
print('RESOURCES #1: ', resp)

http_request('http://localhost:8000/resources/2', method='DELETE')
_, resp = http_request('http://localhost:8000/resources')
print('ALL RESOURCES', resp)


