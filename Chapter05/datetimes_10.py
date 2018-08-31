import datetime

t = datetime.time(13, 30)
d = datetime.date(2018, 1, 11)
result = datetime.datetime.combine(d, t)

print(result)