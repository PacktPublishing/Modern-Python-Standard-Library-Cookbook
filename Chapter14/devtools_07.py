import ast

def run_python(code, mode='evalsafe'):
    if mode == 'evalsafe':
        return ast.literal_eval(code)
    elif mode == 'eval':
        return eval(compile(code, '', mode='eval'))
    elif mode == 'exec':
        return exec(compile(code, '', mode='exec'))
    else:
        raise ValueError('Unsupported execution model {}'.format(mode))


if __name__ == '__main__':
    print(run_python('[1, 2, 3]'))

    try:
        print(run_python('[1, 2, 3][0]'))
    except Exception as e:
        print(e)

    print(run_python('[1, 2, 3][0]', 'eval'))

    try:
        print(run_python('''
def x(): 
    print("printing hello")
x()
''', 'eval'))
    except Exception as e:
        print(e)
    
    print(run_python('''
def x(): 
    print("printing hello")
x()
''', 'exec'))