import urllib.request
import urllib.parse
import json


def http_request(url, query=None, method=None, headers={}, data=None):
    """Perform an HTTP request and return the associated response."""
    parts = vars(urllib.parse.urlparse(url))
    if query:
        parts['query'] = urllib.parse.urlencode(query)

    url = urllib.parse.ParseResult(**parts).geturl()
    r = urllib.request.Request(url=url, method=method, headers=headers,
                               data=data)
    with urllib.request.urlopen(r) as resp:
        msg, resp = resp.info(), resp.read()

    if msg.get_content_type() == 'application/json':
        resp = json.loads(resp.decode('utf-8'))

    return msg, resp


if __name__ == '__main__':
    msg, resp = http_request(
        'https://httpbin.org/get',
        query={
            'a': 'Hello',
            'b': 'World'
        }
    )
    print(msg.get_content_type(), resp)

    msg, resp = http_request('https://httpbin.org/bytes/16')
    print(msg.get_content_type(), resp)

    msg, resp = http_request('https://httpbin.org/post', method='POST',
                            data='This is my posted data!'.encode('ascii'),
                            headers={'Content-Type': 'text/plain'})
    print(msg.get_content_type(), resp)