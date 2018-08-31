from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog


def dialog(ask, title, message=None, **kwargs):
    for widget in (messagebox, simpledialog, filedialog):
        show = getattr(widget, 'ask{}'.format(ask), None)
        if show:
            break
    else:
        raise ValueError('Unsupported type of dialog: {}'.format(ask))

    options = dict(kwargs, title=title)
    for arg, replacement in dialog.argsmap.get(widget, {}).items():
        options[replacement] = locals()[arg]
    return show(**options)
dialog.argsmap = {
    messagebox: {'message': 'message'},
    simpledialog: {'message': 'prompt'}
}


if __name__ == '__main__':
    from tkinter import Tk

    Tk().withdraw()
    for ask in ('okcancel', 'retrycancel', 'yesno', 'yesnocancel',
                'string', 'integer', 'float', 'directory', 'openfilename'):
        choice = dialog(ask, 'This is title', 'What?')
        print('{}: {}'.format(ask, choice))