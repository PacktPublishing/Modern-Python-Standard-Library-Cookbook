import os
from collections import ChainMap

commnad_line_options = {}
config_file_options = {'optname': 'somevalue'}

options = ChainMap(commnad_line_options, os.environ, config_file_options)
value = options.get('optname', 'default-value')
print(value)

import os
from collections import ChainMap, defaultdict

options = ChainMap(commnad_line_options, os.environ, config_file_options,
                    defaultdict(lambda: 'default-value'))
value = options['optname']
value2 = options['other-option']
print(value)
print(value2)