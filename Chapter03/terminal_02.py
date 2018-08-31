import logging, sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide logging file name as argument')
        sys.exit(1)

    logging_file = sys.argv[1]
    logging.basicConfig(level=logging.INFO, filename=logging_file,
                        format='%(asctime)s %(name)s %(levelname)s: %(message)s')

log = logging.getLogger(__name__)

def fibo(num):
    log.info('Computing up to %sth fibonacci number', num)
    a, b = 0, 1
    for n in range(num):
        a, b = b, a+b
        print(b, '', end='')
    print(b)

if __name__ == '__main__':
    import datetime
    fibo(datetime.datetime.now().second)