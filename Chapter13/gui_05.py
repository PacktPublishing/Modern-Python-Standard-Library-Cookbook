import tkinter


def set_menu(window, choices):
    menubar = tkinter.Menu(root)
    window.config(menu=menubar)

    def _set_choices(menu, choices):
        for label, command in choices.items():
            if isinstance(command, dict):
                # Submenu
                submenu = tkinter.Menu(menu)
                menu.add_cascade(label=label, menu=submenu)
                _set_choices(submenu, command)
            elif label == '-' and command == '-':
                # Separator
                menu.add_separator()
            else:
                # Simple choice
                menu.add_command(label=label, command=command)
    
    _set_choices(menubar, choices)


if __name__ == '__main__':
    import sys
    root = tkinter.Tk()

    from collections import OrderedDict
    set_menu(root, {
        'File': OrderedDict([
            ('Open', lambda: print('Open!')),
            ('Save', lambda: print('Save')),
            ('-', '-'),
            ('Quit', lambda: sys.exit(0))
        ])
    })
    root.mainloop()