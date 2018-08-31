import inspect


def inspect_object(o):
    if inspect.isfunction(o) or inspect.ismethod(o):
        print('FUNCTION, arguments:', inspect.signature(o))
    elif inspect.isclass(o):
        print('CLASS, methods:', inspect.getmembers(o, inspect.isfunction))
    else:
        print('OBJECT ({}): {}'.format(
            o.__class__, 
            [(n, v) for n, v in inspect.getmembers(o) if not n.startswith('__')]
        ))



class MyClass:
    def __init__(self):
        self.value = 5

    def sum_to_value(self, other):
        return self.value + other

inspect_object(MyClass.sum_to_value)
# FUNCTION, arguments: (self, other)

inspect_object(MyClass())
# OBJECT (<class '__main__.MyClass'>): [('sum_to_value', <bound method MyClass.sum_to_value of <__main__.MyClass object at 0x107a7a240>>), ('value', 5)]

inspect_object(MyClass)
# CLASS, methods: [('__init__', <function MyClass.__init__ at 0x107bd0400>), ('sum_to_value', <function MyClass.sum_to_value at 0x107bd0488>)]