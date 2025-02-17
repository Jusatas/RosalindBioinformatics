# -*- coding: utf-8 -*-
# Simulates the population of rabbit growth over time.

n = 34  # months
k = 2  # pairs after reproduction

underAged = [0] * n
underAged[0] = 1
adults = [0] * n
rabbitSum = 0

    
print("adults before: " + str(adults[0]))
print("underAged before: " + str(underAged[0]))
print('\n')

for i in range(1, n):
    
    print("adults before: " + str(adults[i]))
    print("underAged before: " + str(underAged[i]))

    adults[i] += underAged[i-1] + adults[i-1]
    underAged[i] = adults[i-1] * k

    
    print("adults after: " + str(adults[i]))
    print("underAged after: " + str(underAged[i]))
    print('\n')
    
rabbitSum = underAged[n - 1] + adults[n - 1]
print(rabbitSum)
