#!/usr/bin/env python3

# Takes in a file containing a pattern
# in the first line and a string in second
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

    parser.add_argument(
            "file", help="File that will be read. Content: pattern, string")
    args = parser.parse_args()

    lines = read_input(args.file).split()
    result = find(lines[0], lines[1])
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
