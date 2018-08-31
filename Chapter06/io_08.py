import xml.etree.ElementTree as ET
from html.parser import HTMLParser


class ETHTMLParser(HTMLParser):
    SELF_CLOSING = {'br', 'img', 'area', 'base', 'col', 'command', 'embed', 'hr',
                    'input', 'keygen', 'link', 'menuitem', 'meta', 'param',
                    'source', 'track', 'wbr'}

    def __init__(self, *args, **kwargs):
        super(ETHTMLParser, self).__init__(*args, **kwargs)
        self._builder = ET.TreeBuilder()
        self._stack = []

    @property
    def _last_tag(self):
        return self._stack[-1] if self._stack else None

    def _handle_selfclosing(self):
        last_tag = self._last_tag
        if last_tag in self.SELF_CLOSING:
            self.handle_endtag(last_tag)

    def handle_starttag(self, tag, attrs):
        self._handle_selfclosing()
        self._stack.append(tag)
        self._builder.start(tag, dict(attrs))

    def handle_endtag(self, tag):
        if tag != self._last_tag:
            self._handle_selfclosing()
        self._stack.pop()
        self._builder.end(tag)

    def handle_data(self, data):
        self._handle_selfclosing()
        self._builder.data(data)

    def close(self):
        return self._builder.close()

text = '''
<html>
    <body class="main-body">
        <p>hi</p>
        <img><br>
        <input type="text" />
    </body>
</html>
'''

parser = ETHTMLParser()
parser.feed(text)
root = parser.close()

print(ET.tostring(root, encoding='unicode'))

def print_node(el, depth=0):
    print(' '*depth, el)
    for child in el:
        print_node(child, depth + 1)
print_node(root)
