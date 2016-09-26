# Jordan Callero
# Project Euler
# February 22, 2016

# This function will take a maximum bound, and find the longest
# Collatz sequence within that range.

def LCS(MaxBound):
    maxChain = 0
    maxChainNum = 0
    currentNumber = 0
    for n in range(MaxBound/3,MaxBound+1):
        currentNumber = n
        currentChain = 0
        if(currentNumber % 2 == 1):
            while(currentNumber != 1):
                if(currentNumber % 2 == 0):
                    currentNumber /= 2
                else:
                    currentNumber = (currentNumber * 3) + 1
                currentChain += 1
        if(currentChain > maxChain):
            maxChain = currentChain
            maxChainNum = n 

    return (maxChainNum, maxChain)
