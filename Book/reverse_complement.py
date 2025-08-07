#!/usr/bin/env python3

# Takes in a DNA string and prints the reverse complement of it.

import sys


def reverse_complement(pattern):
    complemented = "".join(map(complement, pattern))
    return complemented[::-1]


def complement(nucleotide):
    complement_mapping = {
        "A": "T",
        "C": "G",
        "T": "A",
        "G": "C"
    }
    return complement_mapping[nucleotide]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please enter the pattern")
    else:
        print(reverse_complement(sys.argv[1]))
