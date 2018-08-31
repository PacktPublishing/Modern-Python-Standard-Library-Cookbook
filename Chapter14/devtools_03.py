from unittest import mock

def print_division(x, y):
    print(x / y)

if __name__ == '__main__':
    with mock.patch('builtins.print') as mprint:
        print_division(4, 2)
    
    mprint.assert_called_with(2)

    mock_args, mock_kwargs = mprint.call_args
    print(mock_args)
