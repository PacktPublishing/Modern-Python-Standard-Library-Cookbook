import datetime

def shiftmonth(d, months):
    for _ in range(abs(months)):
        if months > 0:
            d = d.replace(day=5) + datetime.timedelta(days=28)
        else:
            d = d.replace(day=1) - datetime.timedelta(days=1)
    d = d.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    return d

now = datetime.datetime.utcnow()
print(now)
print(shiftmonth(now, 1))
print(shiftmonth(now, -1))
print(shiftmonth(now, 10))
