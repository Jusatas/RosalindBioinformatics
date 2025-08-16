#!/usr/bin/env python3

# Takes in a string Genome and forms a an array Skew
# Skew contains the difference between the total number
# of 'G' and 'C' found so far for each position of Skew
# Returns the indexes where Skew has the minimum value
# These values are potential OriC sites.

import argparse
from rosalind_utils import read_input



def main():
    parser = argparse.ArgumentParser(
        description="Return all distinct k-mers forming clumps")

    parser.add_argument("text", help="Full text string or file")
    parser.add_argument("kmer_length", help="How long the k-mers should be")
    parser.add_argument("window_size", help="How big the window should be")
    parser.add_argument("kmer_count", help="How many kmers for a clump")

    args = parser.parse_args()

    text = read_input(args.text)
    kmer_length = int(read_input(args.kmer_length))
    window = int(read_input(args.window_size))
    kmer_count = int(read_input(args.kmer_count))

    result = find_frequent_patterns_clumping(
            text, kmer_length, window, kmer_count)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
