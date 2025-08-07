#!/usr/bin/env python3

import sys


def patternCount(text, pattern):
    """Takes in text, pattern. Outputs how many times the pattern was found"""
    count = 0
    patternLen = len(pattern)

    for i in range(0, len(text) - patternLen):
        currentCheck = text[i:i + patternLen]
        if (currentCheck == pattern):
            count += 1
    return count


def most_frequent_pattern(text, length):
    """Takes in text and length.
    Outputs most frequent pattern of specified length"""
    frequent_patterns = {}
    text_length = len(text)

    for i in range(text_length - length):
        pattern = text[i:i+length]

        if pattern in frequent_patterns:
            frequent_patterns[pattern] += 1
        else:
            frequent_patterns[pattern] = 1


def main():
    if len(sys.argv) != 3:
        print("Please provide the text file and k-mer size")
        sys.exit(1)
    filename = sys.argv[1]
    print(f"Will look for {sys.argv[2]}-mers in {sys.argv[1]}")
    with open(filename, "r") as file:
        dnaString = file.readline().replace("\n", "")
        kmer_length = int(sys.argv[2])

    print(most_frequent_pattern(dnaString, kmer_length))


if __name__ == "__main__":
    main()
