import curses
from curses.textpad import Textbox, rectangle


class TextInput(object):
    @classmethod
    def show(cls, message, content=None):
        return curses.wrapper(cls(message, content)._show)

    def __init__(self, message, content):
        self._message = message
        self._content = content

    def _show(self, stdscr):
        # Set a reasonable size for our input box.
        lines, cols = curses.LINES - 10, curses.COLS - 40

        y_begin, x_begin = (curses.LINES - lines) // 2, (curses.COLS - cols) // 2
        editwin = curses.newwin(lines, cols, y_begin, x_begin)
        editwin.addstr(0, 1, "{}: (hit Ctrl-G to submit)".format(self._message))
        rectangle(editwin, 1, 0, lines-2, cols-1)
        editwin.refresh()

        inputwin = curses.newwin(lines-4, cols-2, y_begin+2, x_begin+1)
        box = Textbox(inputwin)
        self._load(box, self._content)
        return self._edit(box)

    def _load(self, box, text):
        if not text:
            return
        for c in text:
            box._insert_printable_char(c)

    def _edit(self, box):
        while True:
            ch = box.win.getch()
            if not ch:
                continue
            if ch == 127:
                ch = curses.KEY_BACKSPACE
            if not box.do_command(ch):
                break
            box.win.refresh()
        return box.gather()

result = TextInput.show('Insert your name:')
print('Your name:', result)
result = TextInput.show('Insert your name:',
                        content='Some Text\nTo be edited')
print('Your name:', result)