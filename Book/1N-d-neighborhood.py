#!/usr/bin/env python3

# Generate a d-neighborhood - all k-mers (strings of length
# k) whose distance from an input string does not exceed d.
# Can be used with raw strings, files or stdin.

import argparse
from rosalind_utils import read_input
from rosalind_utils import find_hamming

def generate_neighborhood(pattern: str, distance: int) -> set[str]:
    """ Takes in a string pattern and generates all k-mers that
    have a hamming distance smaller than integer distance"""
    if distance == 0:
        return {pattern}

    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    neighborhood = set()

    suffix_neighbors = generate_neighborhood(pattern[1:], distance)

    for neighbor in suffix_neighbors:
        if find_hamming(pattern[1:], neighbor) < distance:
            for nuc in ['A', 'C', 'G', 'T']:
                neighborhood.add(nuc + neighbor)
        else:
            neighborhood.add(pattern[0] + neighbor)   
    
    return neighborhood

def main():
    parser = argparse.ArgumentParser(description="Generate d-neighborhood")

    parser.add_argument(
        "pattern", help="String from which the d-neighborhood is generated.")
    parser.add_argument(
        "distance", help="int representing the maxmium hamming distance")
    args = parser.parse_args()
    pattern = read_input(args.pattern)
    distance = int(read_input(args.distance))

    result = generate_neighborhood(pattern, distance)
    print(" ".join(sorted(result)))


if __name__ == "__main__":
    main()
