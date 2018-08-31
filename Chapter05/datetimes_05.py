import locale
import contextlib
import datetime


@contextlib.contextmanager
def switchlocale(name):
    prev = locale.getlocale()
    locale.setlocale(locale.LC_ALL, name)
    yield
    locale.setlocale(locale.LC_ALL, prev)


def format_date(loc, d):
    with switchlocale(loc):
        fmt = locale.nl_langinfo(locale.D_T_FMT)
        return d.strftime(fmt)

print(format_date('de_DE', datetime.datetime.utcnow()))
print(format_date('en_GB', datetime.datetime.utcnow()))
