# -*- coding: utf-8 -*-
# Reads DNA sequences in FASTA format and calculates
# the most common nucleotide in each position (consesus)

inputArray = []
currentSequence = []

with open("data.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if not line.startswith('>'):
            currentSequence.append(line)
        elif currentSequence:
            inputArray.append(''.join(currentSequence))
            currentSequence = []
    
    # Add the last sequence
    if currentSequence:
        inputArray.append(''.join(currentSequence))

frequency = {
    "A": 0,
    "C": 0,
    "G": 0,
    "T": 0
}

frequencyMatrix = [frequency.copy() for _ in range(len(inputArray[0]))]

for i in range(len(inputArray)):
    for j in range(len(inputArray[i])):
        frequencyMatrix[j][inputArray[i][j]] += 1


mostFrequentLetters = []
for i in range(len(frequencyMatrix)):
    mostFrequentLetter = max(frequencyMatrix[i], key=frequencyMatrix[i].get)
    mostFrequentLetters.append(mostFrequentLetter)


#print("\nFrequency matrix:")
#for i in range(len(frequencyMatrix)):
#    print("Position " + str(i+1) + ": " + str(frequencyMatrix[i]))
    
with open("result.txt", 'w') as file:
    file.write(''.join(mostFrequentLetters) + '\n')
    
    keys = list(frequency.keys())
    for key in keys:
        file.write(key + ":")
        for i in range(len(frequencyMatrix)):
            file.write(" " + str(frequencyMatrix[i].get(key)))
        file.write('\n')


    
    
    

    