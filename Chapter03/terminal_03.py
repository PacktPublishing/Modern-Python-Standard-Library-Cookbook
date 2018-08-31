import logging
import logging.config

# OSX logs through /var/run/syslog this should be /dev/log
# on Linux system or a tuple ('ADDRESS', PORT) to log to a remote server
SYSLOG_ADDRESS = '/var/run/syslog'

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(name)s: %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'syslog': {
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'default',
            'address': SYSLOG_ADDRESS
        }
    },
    'root': {
        'handlers': ['syslog'],
        'level': 'INFO'
    }
})

log = logging.getLogger()
log.info('Hello Syslog!')

# Try to read syslog output
import os
os.system('syslog | tail -n 2')