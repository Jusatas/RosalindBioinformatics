#!/usr/bin/env python3

import argparse
from rosalind_utils import read_input

# Takes in a string a DNA string and an integer kmer_length.
# Calculates how many times each pattern of specified length
# was found using patternCount for all specified length patterns
# and returns those that have been found the most times


def patternCount(text: str, pattern: str):
    """Takes in text, pattern. Outputs how many times the pattern was found"""
    count = 0
    patternLen = len(pattern)

    for i in range(0, len(text) - patternLen + 1):
        currentCheck = text[i:i + patternLen]
        if (currentCheck == pattern):
            count += 1
    return count


def most_frequent_pattern(text: str, pattern_length: int):
    """Takes in text and length.
    Outputs most frequent pattern of specified length"""
    frequent_patterns = []
    text_length = len(text)
    count = []

    for i in range(text_length - pattern_length + 1):
        pattern = text[i:i+pattern_length]
        count.append(patternCount(text, pattern))

    max_count = max(count)
    for i in range(text_length - pattern_length + 1):
        pattern = text[i:i+pattern_length]
        if count[i] == max_count and pattern not in frequent_patterns:
            frequent_patterns.append(pattern)

    return frequent_patterns


def main():
    parser = argparse.ArgumentParser(
            description="Get specific length patterns \
                    that are the most common in a string")
    parser.add_argument(
            "string",
            help="DNA string or file to look inside for patterns")
    parser.add_argument(
            "pattern_length",
            help="Integer specifying how long the patterns should be")

    args = parser.parse_args()

    dnaString = read_input(args.string)
    kmer_length = int(read_input(args.pattern_length))

    patterns = most_frequent_pattern(dnaString, kmer_length)
    for pattern in patterns:
        print(pattern, end=" ")
    print("")


if __name__ == "__main__":
    main()
