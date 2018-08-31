import pathlib
import webbrowser


def playfile(fpath):
    fpath = pathlib.Path(fpath).expanduser().resolve()
    webbrowser.open('file://{}'.format(fpath))


if __name__ == '__main__':
    import sys
    playfile(sys.argv[1])