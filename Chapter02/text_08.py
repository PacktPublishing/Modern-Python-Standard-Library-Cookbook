cols = ['hello world',
        'this is a long text, maybe longer than expected, surely long enough',
        'one more column']
COLSIZE = 20
import textwrap, itertools

def maketable(cols):
    return '\n'.join(map(' | '.join, itertools.zip_longest(*[
        [s.ljust(COLSIZE) for s in textwrap.wrap(col, COLSIZE)] for col in cols
    ], fillvalue=' '*COLSIZE)))

print(maketable(cols))
