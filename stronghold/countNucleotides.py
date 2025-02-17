# -*- coding: utf-8 -*-
# Counts the frequence of nucleotides in a given sequence

with open('data.txt', 'r') as inputFile:
    inputString = inputFile.read().replace('\n','').replace(' ','')
    
print(inputString)

#not adding nucleotide letter automatically:
#nucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
#for i in range(0, len(inputString)):
#    nucleotides[inputString[i]] += 1
    
    
nucleotides = {}
for char in inputString:
    if char in nucleotides:
        nucleotides[char] += 1
    else:
        nucleotides[char] = 1
    
    
print(nucleotides)
        
with open('result.txt', 'w') as outputFile:
    for key, value in nucleotides.items():
        outputFile.write(str(value) + ' ')