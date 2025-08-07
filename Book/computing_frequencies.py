#!/usr/bin/env python3

import sys


def computing_frequencies(text, k):
    """Takes in text and length of a pattern (k).
    Outputs how often all possible patterns are present."""

    frequency_array = []
    for i in range(pow(4, k)):  # goes up to 4^k - 1
        frequency_array.append(0)

    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        j = pattern_to_num(pattern)
        frequency_array[j] += 1

    return frequency_array


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


def main():
    if len(sys.argv) != 2:
        print("Please provide a filename with a DNA string and k for k-mers")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as file:
        dnaString = file.readline().replace("\n", "")
        kmer = int(file.readline().replace("\n", ""))

    for frequency in computing_frequencies(dnaString, kmer):
        print(frequency, end=" ")
    print("")


if __name__ == "__main__":
    main()
