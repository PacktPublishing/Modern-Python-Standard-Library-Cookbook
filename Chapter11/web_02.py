import urllib.parse

def parse_url(url):
    """Parses an URL of the most widspread format.

    This takes for granted there is a single set of parameters
    for the whole path.
    """
    parts = urllib.parse.urlparse(url)
    parsed = vars(parts)
    parsed['query'] = urllib.parse.parse_qs(parts.query)
    return parsed

url = 'http://user:pwd@host.com:80/path/subpath?arg1=val1&arg2=val2#fragment'
result = parse_url(url)
print(result)
