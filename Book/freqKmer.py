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


def main():
    if len(sys.argv) != 2:
        print("Please specify one data file")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        dnaString = file.readline().replace("\n", "")
        kmer = file.readline().replace("\n", "")

    print(patternCount(dnaString, kmer))


if __name__ == "__main__":
    main()
