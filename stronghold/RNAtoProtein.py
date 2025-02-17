# -*- coding: utf-8 -*-
# Converts RNA sequences to proteins


with open("codonTable.txt", 'r') as file:
    linesList = file.readlines()
    
words = " ".join(linesList)

wordsList = words.split()
    
codons = {}

for i in range(0, len(wordsList), 2):
    codon = wordsList[i]
    protein = wordsList[i + 1]
    
    codons.update( {codon : protein} )
    
        
with open("data.txt", 'r') as file:
    line = file.readline()
    
proteinString = ""
for i in range(0, len(line), 3):
    codonTriplet = line[i:i+3]
    
    protein = codons.get(codonTriplet)

    if(protein.lower() != "stop"): #remove to leave Stop codon in string
        proteinString += protein  
    else:
        break
    
print(proteinString)
    
with open("result.txt", 'w') as file:
    file.write(proteinString)
    
    