import datetime

def workdays(d, end, excluded=(6, 7)):
    days = []
    while d.date() < end.date():
        if d.isoweekday() not in excluded:
            days.append(d)
        d += datetime.timedelta(days=1)
    return days

print(workdays(datetime.datetime(2018, 3, 22), 
               datetime.datetime(2018, 3, 26)))
