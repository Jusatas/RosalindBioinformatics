# -*- coding: utf-8 -*-
# Calculates the hamming distance of two DNA sequences

with open('data.txt', 'r') as inputFile:
    inputLine1 = inputFile.readline().strip()
    inputLine2 = inputFile.readline().strip()
    

hamDist = 0

for i in range(0, len(inputLine1)):
    if (inputLine1[i] != inputLine2[i]):
        hamDist += 1
        
print(hamDist)