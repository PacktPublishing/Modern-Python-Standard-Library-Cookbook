import shelve

with shelve.open('/tmp/shelf.db') as shelf:
  shelf['value'] = 5

with shelve.open('/tmp/shelf.db') as shelf:
  print(shelf['value'])

class MyClass(object):
  def __init__(self, value):
    self.value = value

with shelve.open('/tmp/shelf.db') as shelf:
  shelf['value'] = MyClass(5)

with shelve.open('/tmp/shelf.db') as shelf:
  print(shelf['value'])

with shelve.open('/tmp/shelf.db') as shelf:
  print(shelf['value'].value)
