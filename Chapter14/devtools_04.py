import logging
import logging.handlers
import functools

crashlogger = logging.getLogger('__crashes__')

def configure_crashreport(mailhost, fromaddr, toaddrs, subject, 
                          credentials, tls=False):
    if configure_crashreport._configured:
        return
    
    crashlogger.addHandler(
        logging.handlers.SMTPHandler(
            mailhost=mailhost,
            fromaddr=fromaddr,
            toaddrs=toaddrs,
            subject=subject,
            credentials=credentials,
            secure=tuple() if tls else None
        )
    )
    configure_crashreport._configured = True
configure_crashreport._configured = False


def crashreport(f):
    @functools.wraps(f)
    def _crashreport(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            crashlogger.exception(
                '{} crashed\n'.format(f.__name__)
            )
            raise
    return _crashreport


if __name__ == '__main__':
    @crashreport
    def main():
        3 / 0

    configure_crashreport(
        'your-smtp-host.com',
        'no-reply@your-smtp-host.com',
        'crashes_receiver@another-smtp-host.com',
        'Automatic Crash Report from TestApp',
        ('smtpserver_username', 'smtpserver_password'),
        tls=True
    )
    main()