# Jordan Callero
# Project Euler
# April 20, 2016

# Problem 21, will sum all of the Amicable numbers below MaxNum
# Amicable numbers are numbers where the factors added are a number
#      x, and the addition of the factors of x come back to the
#      original number

def sumAmiNum(maxNum):
    total = 0
    for i in range(1,maxNum):
        factorList = factors(i)
        factorTotal = sum(factorList) - i
        if(factorTotal < maxNum and
           factorTotal > 1 and
           factorTotal != i):
            factorList2 = factors(factorTotal)
            factorTotal2 = sum(factorList2) - factorTotal
            if(i == factorTotal2):
                print(i, factorTotal, factorTotal2)
                total += i
    return total


def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
