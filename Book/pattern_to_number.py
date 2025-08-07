#!/usr/bin/env python3

# Takes in a pattern composed of the four DNA letters
# Returns a unique numeric index for

import sys


def pattern_to_num(pattern):
    """Takes in a pattern and returns the index that is used
    to find the pattern in all possible patterns of ACGT"""

    nuc_values = {
        "A": 0,
        "C": 1,
        "G": 2,
        "T": 3
    }
    num = 0

    start_i = len(pattern)
    i = start_i
    for letter in pattern:
        i -= 1
        num += nuc_values[letter] * pow(4, i)

    return num


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a pattern to turn into a number")
    else:
        print(pattern_to_num(sys.argv[1]))
