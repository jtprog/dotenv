"""Main file for Dotenv module"""
import argparse
from dotenv import get_variable, set_variable, get_variables, __version__


PARSER = argparse.ArgumentParser()

PARSER.add_argument("key", nargs='?')
PARSER.add_argument("value", nargs='?')

PARSER.add_argument('--file', default='.env')

PARSER.add_argument('--version', action='version', version=__version__)

PARSER.add_argument('--shell', action='store_true', default=False)

ARGS = PARSER.parse_args()


if ARGS.shell:
    PRINT_FORMAT = '%s=%s'
else:
    PRINT_FORMAT = '%s: %s'

if ARGS.key is None:
    for key, value in get_variables(ARGS.file).items():
        print(PRINT_FORMAT % (key, value))
elif ARGS.value is None:
    print(PRINT_FORMAT % (ARGS.key, get_variable(ARGS.file, ARGS.key)))
else:
    set_variable(ARGS.file, ARGS.key, ARGS.value)
    print(PRINT_FORMAT % (ARGS.key, ARGS.value))
