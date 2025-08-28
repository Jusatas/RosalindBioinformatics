import os
import sys


def read_input(arg):
    """
    Reads input from file, stdin or just reads a raw string,
    Strips leading, trailing whitespace and returns result.
    """
    if arg == "-":
        return sys.stdin.read().strip()

    if os.path.isfile(arg):
        with open(arg) as file:
            return file.read().strip()

    else:
        return arg.strip()


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


def generate_neighborhood(pattern: str, distance: int) -> set[str]:
    """ Takes in a string pattern and returns a set of all k-mers that
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


def find_hamming(string1: str, string2: str) -> int:
    """Takes in two DNA strings, return the hamming distance
    between them - how many mismatches there are."""
    mismatches = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            mismatches += 1
    return mismatches


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


def number_to_pattern(index, length):
    nuc_values = {
        0: "A",
        1: "C",
        2: "G",
        3: "T"
    }
    pattern = []

    for _ in range((length)):
        num = index

        index = index // 4  # integer division
        remainder = num % 4
        letter = nuc_values[remainder]
        pattern.insert(0, letter)  # prepends the letter

    return "".join(pattern)  # return a string

