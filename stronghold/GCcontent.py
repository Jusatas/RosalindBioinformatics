

highestCGname = ""
highestPercentage = 0
CGname = ""
CGcount = 0
totalCount = 0

with open('data.txt', 'r') as inputFile:
    inputLine = inputFile.readline().strip()
    while inputLine:
        CGname = inputLine
        totalCount = 0
        CGcount = 0
        
        inputLine = ''
        inputChar = inputFile.read(1)
        while inputChar and inputChar != '>':
            
            if (inputChar != '\n'):
                inputLine += inputChar
                totalCount += 1
                if (inputChar == 'C' or inputChar == 'G'):
                    CGcount += 1
                
            inputChar = inputFile.read(1)

        percentage = CGcount / totalCount * 100
        
        if (percentage > highestPercentage):
            highestPercentage = percentage
            highestCGname = CGname

        inputLine = inputFile.readline().strip()
        
highestPercentage = round(highestPercentage, 6)
print('\n\n')
print(highestCGname)
print(f"{highestPercentage:.6f}")


