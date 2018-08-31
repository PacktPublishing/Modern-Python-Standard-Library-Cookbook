import datetime

def parse_iso8601(strdate):
    date, time = strdate.split('T', 1)
    if '-' in time:
        time, tz = time.split('-')
        tz = '-' + tz
    elif '+' in time:
        time, tz = time.split('+')
        tz = '+' + tz
    elif 'Z' in time:
        time = time[:-1]
        tz = '+0000'
    date = date.replace('-', '')
    time = time.replace(':', '')
    tz = tz.replace(':', '')
    return datetime.datetime.strptime('{}T{}{}'.format(date, time, tz),
                                      "%Y%m%dT%H%M%S%z")

print(parse_iso8601('2018-03-19T22:00Z'))
print(parse_iso8601('2018-03-19T2200Z'))
print(parse_iso8601('2018-03-19T22:00:03Z'))
print(parse_iso8601('20180319T22:00:03Z'))
print(parse_iso8601('20180319T22:00:03+05:00'))
print(parse_iso8601('20180319T22:00:03+0500'))
