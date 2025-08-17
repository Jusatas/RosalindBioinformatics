#!/usr/bin/env python3

from rosalind_utils import find_hamming, read_input
import argparse


def main():
    pass
    parser = argparse.ArgumentParser(
            description="Find starting positions where pattern is\
                    inside text with at most mismatch_count mismatches")
    parser.add_argument("pattern", help="String to look for")
    parser.add_argument("text", help="Full text to look in")
    parser.add_argument("mismatch_count",
                        help="The amount of mismatches allowed")

    args = parser.parse_args()

    pattern = read_input(args.pattern)
    text = read_input(args.text)
    mismatch_count = int(read_input(args.mismatch_count))

    result = match(pattern, text, mismatch_count)
    print(" ".join(map(str, result)))


def match(pattern: str, text: str, mismatch_count: int):
    """Return all starting positions where pattern appears
    as a substring of text with at most mismatch_count mismatches
    pass"""

    matches = []
    pattern_len = len(pattern)

    for i in range(len(text) - pattern_len):
        substring = text[i:i + pattern_len]
        if find_hamming(substring, pattern) <= mismatch_count:
            matches.append(i)

    return matches


if __name__ == "__main__":
    main()
