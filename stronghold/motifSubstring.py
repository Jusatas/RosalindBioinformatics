# -*- coding: utf-8 -*-
# Finds a specific DNA motif inside a sequence

with open("data.txt", 'r') as file:
    dnaString = file.readline().strip()
    motif = file.readline().strip()
    
print(dnaString)
print(motif)

motifLength = len(motif)
motifLocations = []
for i in range(0, len(dnaString)):
    print(str(i) + " " + dnaString[i:i+motifLength] + " " + motif, end = '')
    if(dnaString[i:i+motifLength] == motif):
        print(" Motif found! ")
        motifLocations.append(i+1)
    else:
        print('')
        
with open("result.txt", 'w') as file:
    for loc in motifLocations:
        file.write(str(loc) + " ")
