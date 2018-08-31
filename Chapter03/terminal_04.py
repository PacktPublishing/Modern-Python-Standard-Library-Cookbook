import argparse
import operator
import logging
import functools

parser = argparse.ArgumentParser(
    description='Applies an operation to one or more numbers'
)
parser.add_argument("number",
                    help="One or more numbers to perform an operation on.",
                    nargs='+', type=int)
parser.add_argument('-o', '--operation',
                    help="The operation to perform on numbers.",
                    choices=['add', 'sub', 'mul', 'div'], default='add')
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")

opts = parser.parse_args()

logging.basicConfig(level=logging.INFO if opts.verbose else logging.WARNING)
log = logging.getLogger()

operation = getattr(operator, opts.operation)
log.info('Applying %s to %s', opts.operation, opts.number)
print(functools.reduce(operation, opts.number))
