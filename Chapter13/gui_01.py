from tkinter import messagebox, Tk
 

def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')
    
    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)


if __name__ == '__main__':
    Tk().withdraw()
    alert('Hello', 'Hello World')
    alert('Hello Again', 'Hello World 2', kind='warning')