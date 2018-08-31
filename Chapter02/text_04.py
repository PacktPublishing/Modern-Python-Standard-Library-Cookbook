import string

class TemplateFormatter(string.Formatter):
    def get_field(self, field_name, args, kwargs):
        if field_name.startswith("$"):
            code = field_name[1:]
            val = eval(code, {}, dict(kwargs))
            return val, field_name
        else:
            return super(TemplateFormatter, self).get_field(field_name, args, kwargs)
messages = ['Message 1', 'Message 2']

tmpl = TemplateFormatter()
txt = tmpl.format("Hello {name}, "
                  "You have {$len(messages)} message{$len(messages) and 's'}:\n{$'\\n'.join(messages)}",
                  name='Alessandro', messages=messages)
print(txt)
