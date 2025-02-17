# -*- coding: utf-8 -*-
# Finds the reverse complement of a DNA sequence

with open('data.txt', 'r') as inputFile:
    inputString = inputFile.read().replace('\n','').replace(' ','')
    
print(inputString)

inputString = inputString.replace('T','X').replace('G','Y')
inputString = inputString.replace('A','T').replace('C','G').replace('Y','C').replace('X','A')

inputString = inputString[::-1]

print(inputString)
     
with open('result.txt', 'w') as outputFile:
    outputFile.write(inputString)