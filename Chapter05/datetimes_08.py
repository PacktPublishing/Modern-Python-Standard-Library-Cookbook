import datetime

def monthweekdays(month, weekday):
    now = datetime.datetime.utcnow()
    d = now.replace(day=1, month=month, hour=0, minute=0, second=0, microsecond=0)
    days = []
    while d.month == month:
        if d.isoweekday() == weekday:
            days.append(d)
        d += datetime.timedelta(days=1)
    return days

print(monthweekdays(3, 1))
print(monthweekdays(3, 1)[2])
