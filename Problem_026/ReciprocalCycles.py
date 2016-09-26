# Jordan Callero
# Project Euler
# September 23, 2016

# Reciprocal Cycles, given the number n. Figure out which fraction
#  1/n has the longest repeating decimal

import re
import decimal

def recCycle(n):
    maxRepeat = 1
    maxNumber = -1
    for p in range(1,n+1):
        temp = cycleCount(p)
        if (temp > maxRepeat):
            maxRepeat = temp
            maxNumber = p
    return(maxNumber, maxRepeat)

def cycleCount(p):
    num = str(Decimal(1) / Decimal(p))

