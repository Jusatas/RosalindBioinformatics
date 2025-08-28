#!/usr/bin/env python3

# Takes in a string of text representing a genome,
# integers representing k-mer length, clump window
# size and how many times the k-mer must occur.
# Returns all k-mers that satisfied theese conditions.


# Problem URL: https://rosalind.info/problems/ba1e/

import argparse
from rosalind_utils import read_input
from rosalind_utils import computing_frequencies
from rosalind_utils import pattern_to_num, number_to_pattern


def find_frequent_patterns_clumping(text, kmer_length, window, kmer_count):
    """ takes in text, the length of kmers to be used, the size of window,
    and how many kmers are enough, returns all such kmers"""

    frequent_patterns = set()
    possible_kmers = pow(4, kmer_length)
    first_window = text[0:window]
    frequency_array = computing_frequencies(first_window, kmer_length)
    clump = [0] * possible_kmers

    for i in range(possible_kmers):
        if frequency_array[i] >= kmer_count:  # Enough kmers for clump
            clump[i] = 1

    for i in range(1, len(text) - window + 1):
        first_pattern = text[i-1:i-1+kmer_length]
        index = pattern_to_num(first_pattern)
        frequency_array[index] -= 1

        last_pattern = text[i+window-kmer_length:i+window]
        index = pattern_to_num(last_pattern)
        frequency_array[index] += 1
        if frequency_array[index] >= kmer_count:
            clump[index] = 1

    for i in range(possible_kmers):
        if clump[i] == 1:
            pattern = number_to_pattern(i, kmer_length)
            frequent_patterns.add(pattern)

    return list(frequent_patterns)


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
