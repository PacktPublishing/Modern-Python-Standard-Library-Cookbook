import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def calculate(expression):
    parts = expression.split()

    try:
        result = int(parts[0])
    except:
        raise ValueError('First argument of expression must be numberic')

    operator = None
    for part in parts[1:]:
        try:
            num = int(part)
            if operator is None:
                raise ValueError('No operator proviede for the numbers')
        except ValueError:
            if operator:
                raise ValueError('operator already provided')
            operator = operators[part]
        else:
            result = operator(result, num)
            operator = None

    return result

print(calculate('5 + 3'))

print(calculate('1 + 2 + 3'))

print(calculate('3 * 2 + 4'))
