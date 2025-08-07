#!/usr/bin/env python3

import sys


def patternCount(text, pattern):
    """Takes in text, pattern. Outputs how many times the pattern was found"""
    count = 0
    patternLen = len(pattern)

    for i in range(0, len(text) - patternLen + 1):
        currentCheck = text[i:i + patternLen]
        if (currentCheck == pattern):
            count += 1
    return count


def most_frequent_pattern(text, length):
    """Takes in text and length.
    Outputs most frequent pattern of specified length"""
    frequent_patterns = []
    text_length = len(text)
    count = []

    for i in range(text_length - length + 1):
        pattern = text[i:i+length]
        count.append(patternCount(text, pattern))

    max_count = max(count)
    for i in range(text_length - length + 1):
        pattern = text[i:i+length]
        if count[i] == max_count and pattern not in frequent_patterns:
            frequent_patterns.append(pattern)

    return frequent_patterns


def main():
    if len(sys.argv) != 3:
        print("Please provide the text file and k-mer size")
        sys.exit(1)
    filename = sys.argv[1]
    print(f"Will look for {sys.argv[2]}-mers in {sys.argv[1]}")
    with open(filename, "r") as file:
        dnaString = file.readline().replace("\n", "")
        kmer_length = int(sys.argv[2])

    patterns = most_frequent_pattern(dnaString, kmer_length)
    for pattern in patterns:
        print(pattern, end=" ")
    print("")


if __name__ == "__main__":
    main()
