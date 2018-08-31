import datetime

ts = 1521588268
d = datetime.datetime.utcfromtimestamp(ts)
print(repr(d))

newts = d.timestamp()
print(newts)
