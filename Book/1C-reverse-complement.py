#!/usr/bin/env python3

# Takes in a raw string, file or stdin DNA string,
# Finds and returns the rever complement
import sys


def reverse_complement(pattern: str) -> str:
    """ Takes in a string representing a DNA sequence, 
    returns its reverse complement string """

    complemented = "".join(map(complement, pattern))
    return complemented[::-1]


def complement(nucleotide: str) -> str:
    """Takes in a single character string representing
    a nucleotide, returns its complement"""

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
