import datetime

def asutc(d):
    return d.astimezone(datetime.timezone.utc)

now = datetime.datetime.now().replace(
   tzinfo=datetime.timezone(datetime.timedelta(hours=1))
)
print(now)

print(asutc(now))
