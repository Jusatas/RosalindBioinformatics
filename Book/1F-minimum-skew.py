#!/usr/bin/env python3

# Takes in a string Genome and forms a an array Skew
# Skew contains the difference between the total number
# of 'G' and 'C' found so far for each position of Skew
# Returns the indices where Skew has the minimum value
# These values are potential OriC sites.

import argparse
from rosalind_utils import read_input


def find_skew(genome):
    """Takes in a string genome, returns a skew array
    and and array containing it's minimum value indices"""
    skew = [0]
    min_value_indices = []
    min_value = 0

    for i, nucleotide in enumerate(genome):
        if nucleotide == "C":
            skew.append(skew[-1] - 1)
        elif nucleotide == "G":
            skew.append(skew[-1] + 1)
        else:
            skew.append(skew[-1])

        if skew[-1] < min_value:
            min_value = skew[-1]
            min_value_indices[:] = [i + 1]
        elif skew[-1] == min_value:
            min_value_indices.append(i + 1)

    return skew, min_value_indices


def main():
    parser = argparse.ArgumentParser(
        description="Return all distinct k-mers forming clumps")

    parser.add_argument(
            "genome",
            help="String containing string repesenting a genome")
    args = parser.parse_args()

    genome = read_input(args.genome)
    result = (find_skew(genome)[1])
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
