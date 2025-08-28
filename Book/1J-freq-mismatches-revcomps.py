#!/usr/bin/env python3

# Reads raw arguments,
# Finds the most common k-mers of specified length taking into
# account their reverse complements and allowing a specified
# amount of mismatches
# Problem url: https://rosalind.info/problems/ba1j/

import argparse
from rosalind_utils import (read_input, pattern_to_num, 
    number_to_pattern, generate_neighborhood)

def find_words(text: str, wordlength: int, mismatches: int) -> set[str]:
    """ Takes in a string of text, finds the most frequent words of length
    int wordlength that have at most int mismatches. Also counts their 
    reverse complements. Returns them in a set"""

    freq_words = set()
    neighbordhoods = [] # List of lists of words and their similar neighbors
    neighbors = [] # Flattened neighborhoods list
    for i in range(len(text) - wordlength + 1):
        neighborhood = generate_neighborhood(text[i:i+wordlength], mismatches)
        neighbordhoods.append(neighborhood)
        
        for neighbor in neighborhood:
            neighbors.append(neighbor)

    neighbors_amount = len(neighbors)
    index = [0] * neighbors_amount
    amount = [1] * neighbors_amount
    for i in range(neighbors_amount):
        pattern = neighbors[i]
        index[i] = pattern_to_num(pattern)

    sorted_index = sorted(index)
    for i in range(neighbors_amount - 1):
        if sorted_index[i] == sorted_index[i+1]:
            amount[i+1] = amount[i] + 1

    maxAmount = max(amount)

    for i in range(neighbors_amount - 1):
        if amount[i] == maxAmount:
            pattern = number_to_pattern(sorted_index[i], wordlength)
            freq_words.add(pattern)

    return freq_words

def main():
    parser = argparse.ArgumentParser(description="Get the"
        "most frequent words with mismatches")

    parser.add_argument("text", help="String containing the full text")
    parser.add_argument("wordlength", help="Int indicating the length of words")
    parser.add_argument("mismatches", help="Int indicating amount of allowed mismatches")
    args = parser.parse_args()

    text = read_input(args.text)
    wordlength = int(read_input(args.wordlength))
    mismatches = int(read_input(args.mismatches))

    result = find_words(text, wordlength, mismatches) 
    print(" ".join(sorted(result)))

if __name__ == "__main__":
    main()
