# -*- coding: utf-8 -*-
# Calculates the probability that two randomly chosen individuals
#  from a population will produce an offspring with a dominant phenotype.

def calculateDom(homoDomAmount, heteroAmount, homoRecAmount):
    total = homoDomAmount + heteroAmount + homoRecAmount

    twoHomoRec = (homoRecAmount / total) * ((homoRecAmount - 1) / (total - 1))
    twoHetero = (heteroAmount / total) * ((heteroAmount - 1) / (total - 1))
    heteroRec = (homoRecAmount / total) * (heteroAmount / (total - 1))
    recHetero = (heteroAmount / total) * (homoRecAmount / (total - 1))
    
    recProbability = twoHomoRec + 0.25 * twoHetero + 0.5 * heteroRec + 0.5 * recHetero

    domProbability = 1 - recProbability
    
    return domProbability

with open("data.txt", 'r') as file:
    line = file.readline()
    data = line.split()
    homoDomAmount, heteroAmount, homoRecAmount = map(int, data)
    print(homoDomAmount, heteroAmount, homoRecAmount)

print(calculateDom(homoDomAmount, heteroAmount, homoRecAmount))

