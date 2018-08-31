import string
import cgi

class HTMLFormatter(string.Formatter):
    def get_field(self, field_name, args, kwargs):
        val, key = super(HTMLFormatter, self).get_field(field_name, args, kwargs)
        if hasattr(val, '__html__'):
            val = val.__html__()
        elif isinstance(val, str):
            val = cgi.escape(val)
        return val, key


class Markup:
    def __init__(self, v):
        self.v = v
    def __str__(self):
        return self.v
    def __html__(self):
        return str(self)


html = HTMLFormatter().format('Hello {name}, you are {title}', 
                              name='<strong>Name</strong>',
                              title=Markup('<em>a developer</em>'))
print(html)