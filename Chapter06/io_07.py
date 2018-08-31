import xml.etree.ElementTree as ET
from contextlib import contextmanager


class XMLDocument(object):
    def __init__(self, root='document', mode='xml'):
        self._root = ET.Element(root)
        self._mode = mode

    def __str__(self):
        return ET.tostring(self._root, encoding='unicode', method=self._mode)

    def write(self, fobj):
        ET.ElementTree(self._root).write(fobj)

    def __enter__(self):
        return XMLDocumentBuilder(self._root)

    def __exit__(self, exc_type, value, traceback):
        return


class XMLDocumentBuilder(object):
    def __init__(self, root):
        self._current = [root]

    def tag(self, *args, **kwargs):
        el = ET.Element(*args, **kwargs)
        self._current[-1].append(el)
        @contextmanager
        def _context():
            self._current.append(el)
            try:
                yield el
            finally:
                self._current.pop()
        return _context()

    def text(self, text):
        if self._current[-1].text is None:
            self._current[-1].text = ''
        self._current[-1].text += text
doc = XMLDocument('html', mode='html')

with doc as _:
    with _.tag('head'):
        with _.tag('title'): _.text('This is the title')
    with _.tag('body'):
        with _.tag('div', id='main-div'):
            with _.tag('h1'): _.text('My Document')
            with _.tag('strong'): _.text('Hello World')
            _.tag('img', src='http://via.placeholder.com/150x150')

print(doc)
