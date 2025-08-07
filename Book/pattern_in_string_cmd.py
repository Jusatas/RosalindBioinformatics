#!/usr/bin/env python3

# Takes in a pattern and a string
# Returns all starting positions
# of pattern that were found in string.

# Problem URL: https://rosalind.info/problems/ba1d/

import argparse
from rosalind_utils import read_input


def find(pattern, string):
    locations = []
    cursor = 0

    while True:
        cursor = string.find(pattern, cursor)
        if cursor == -1:
            return locations
        locations.append(cursor)
        cursor += 1


def main():
    parser = argparse.ArgumentParser(
             description="Return pattern occurance indexes in text")

    parser.add_argument("pattern", help="Pattern string or file")
    parser.add_argument("text", help="Full text string or file")
    args = parser.parse_args()

    pattern = read_input(args.pattern)
    text = read_input(args.text)

    result = find(pattern, text)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
