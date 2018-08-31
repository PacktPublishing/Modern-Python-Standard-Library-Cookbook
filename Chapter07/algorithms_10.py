from functools import singledispatch

@singledispatch
def human_readable(d):
    raise ValueError('Unsupported argument type %s' % type(d))

@human_readable.register(dict)
def human_readable_dict(d):
    for key, value in d.items():
        print('{}: {}'.format(key, value))

@human_readable.register(list)
@human_readable.register(tuple)
def human_readable_list(d):
    for key, value in d:
        print('{}: {}'.format(key, value))

human_readable({'name': 'Tifa', 'surname': 'Lockhart'})

human_readable([('name', 'Nobuo'), ('surname', 'Uematsu')])

try:
    human_readable(5)
except Exception as e:
    print(e)
