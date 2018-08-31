from collections import OrderedDict

attrs = OrderedDict([('id', 'header'), ('style', 'background-color:red')])    
print(
    '<span {}>'.format(' '.join('%s="%s"' % a for a in attrs.items()))
)
