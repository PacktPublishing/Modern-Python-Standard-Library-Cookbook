import shutil
import textwrap, itertools

def maketable(cols):
    term_size = shutil.get_terminal_size(fallback=(80, 24))
    colsize = (term_size.columns // len(cols)) - 3
    if colsize < 1:
        raise ValueError('Column too small')
    return '\n'.join(map(' | '.join, itertools.zip_longest(*[
        [s.ljust(colsize) for s in textwrap.wrap(col, colsize)] for col in cols
    ], fillvalue=' '*colsize)))
COLUMNS = 5
TEXT = ['Lorem ipsum dolor sit amet, consectetuer adipiscing elit. '
        'Aenean commodo ligula eget dolor. Aenean massa. '
        'Cum sociis natoque penatibus et magnis dis parturient montes, '
        'nascetur ridiculus mus'] * COLUMNS

print(maketable(TEXT))