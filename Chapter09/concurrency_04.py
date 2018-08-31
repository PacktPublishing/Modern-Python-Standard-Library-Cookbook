import concurrent.futures
import urllib.request
import time

def benchmark_url(url):
    begin = time.time()
    with urllib.request.urlopen(url) as conn:
        conn.read()
    return (time.time() - begin, url)

class UrlsBenchmarker(object):
    def __init__(self, urls):
        self._urls = urls

    def run(self, executor):
        futures = self._benchmark_urls(executor)
        fastest = min([
            future.result() for future in
                concurrent.futures.as_completed(futures)
        ])
        print('Fastest Url: {1}, in {0}'.format(*fastest))

    def _benchmark_urls(self, executor):
        futures = []
        for url in self._urls:
            future = executor.submit(benchmark_url, url)
            future.add_done_callback(self._print_timing)
            futures.append(future)
        return futures

    def _print_timing(self, future):
        print('Url {1} downloaded in {0}'.format(
            *future.result()
        ))


import concurrent.futures
with concurrent.futures.ThreadPoolExecutor() as executor:
    UrlsBenchmarker([
            'http://time.com/',
            'http://www.cnn.com/',
            'http://www.facebook.com/',
            'http://www.apple.com/',
    ]).run(executor)
