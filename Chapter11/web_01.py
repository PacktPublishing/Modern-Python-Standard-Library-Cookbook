import json
import datetime
import decimal
import types


class CustomJSONEncoder(json.JSONEncoder):
    """JSON Encoder with support for additional types.

    Supports dates, times, decimals, generators and
    any custom class that implements __json__ method.
    """
    def default(self, obj):
        if hasattr(obj, '__json__') and callable(obj.__json__):
            return obj.__json__()
        elif isinstance(obj, (datetime.datetime, datetime.time)):
            return obj.replace(microsecond=0).isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, types.GeneratorType):
            return list(obj)
        else:
            return super().default(obj)



jsonstr = json.dumps({'s': 'Hello World',
                      'dt': datetime.datetime.utcnow(),
                      't': datetime.datetime.utcnow().time(),
                      'g': (i for i in range(5)),
                      'd': datetime.date.today(),
                      'dct': {
                          's': 'SubDict',
                          'dt': datetime.datetime.utcnow()
                      }}, 
                     cls=CustomJSONEncoder)
print(jsonstr)

print(json.loads(jsonstr))

class CustomJSONDecoder(json.JSONDecoder):
    """Custom JSON Decoder that tries to decode additional types.

    Decoder tries to guess dates, times and datetimes in ISO format.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs, object_hook=self.parse_object
        )

    def parse_object(self, values):
        for k, v in values.items():
            if not isinstance(v, str):
                continue
            
            if len(v) == 10 and v.count('-') == 2:
                # Probably contains a date
                try:
                    values[k] = datetime.datetime.strptime(v, '%Y-%m-%d').date()
                except:
                    pass
            elif len(v) == 8 and v.count(':') == 2:
                # Probably contains a time
                try:
                    values[k] = datetime.datetime.strptime(v, '%H:%M:%S').time()
                except:
                    pass
            elif (len(v) == 19 and v.count('-') == 2 and 
                  v.count('T') == 1 and v.count(':') == 2):
                # Probably contains a datetime
                try:
                    values[k] = datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
                except:
                    pass
        return values



jsondoc = json.loads(jsonstr, cls=CustomJSONDecoder)
print(jsondoc)