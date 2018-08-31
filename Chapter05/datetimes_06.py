import datetime

def shiftdate(d, days):
    return (
        d.replace(hour=0, minute=0, second=0, microsecond=0) +
        datetime.timedelta(days=days)
    )

now = datetime.datetime.utcnow()
print(now)
print(shiftdate(now, 1))
print(shiftdate(now, -1))
print(shiftdate(now, 11))
