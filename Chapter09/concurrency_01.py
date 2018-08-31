def fetch_url(url):
    """Fetch content of a given url from the web"""
    import urllib.request
    response = urllib.request.urlopen(url)
    return response.read()


def wait_until(predicate):
    """Waits until the given predicate returns True"""
    import time
    seconds = 0
    while not predicate():
        print('Waiting...')
        time.sleep(1.0)
        seconds += 1
    print('Done!')
    return seconds


from multiprocessing.pool import ThreadPool
pool = ThreadPool(4)
t1 = pool.apply_async(fetch_url, args=('https://httpbin.org/delay/3',))
t2 = pool.apply_async(wait_until, args=(t1.ready, ))
pool.close()
pool.join()
print('Total Time:', t2.get())
print('Content:', t1.get())
