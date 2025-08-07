import os
import sys


def read_input(arg):
    """
    Reads input from file, stdin or just reads a raw string,
    Strips leading, trailing whitespace and returns result.
    """
    if arg == "-":
        return sys.stdin.read().strip()

    if os.path.isfile(arg):
        with open(arg) as file:
            return file.read().strip()

    else:
        return arg.strip()
