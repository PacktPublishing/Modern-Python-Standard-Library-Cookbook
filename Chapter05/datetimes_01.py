import datetime

def now():
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
def astimezone(d, offset):
    return d.astimezone(datetime.timezone(datetime.timedelta(hours=offset)))

d = now()
print(d)

d = astimezone(d, 1)
print(d)
