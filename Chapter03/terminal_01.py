import logging, sys

logging.basicConfig(level=logging.INFO, stream=sys.stderr,
                    format='%(asctime)s %(name)s %(levelname)s: %(message)s')
log = logging.getLogger(__name__)

def dosum(a, b, count=1):
    log.info('Starting sum')
    if a == b == 0:
        log.warning('Will be just 0 for any count')
    res = (a + b) * count
    log.info('(%s + %s) * %s = %s' % (a, b, count, res))
    print(res)

dosum(5, 3)

dosum(5, 3, count=2)

dosum(0, 1, count=5)

dosum(0, 0)
