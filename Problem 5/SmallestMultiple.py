# Jordan Callero
# February 3, 2016
# Project Euler #5

# Given a number n, this function will return the smallest number that divides
# All of those numbers evenly

def smallestMultiple(MaxNum):
    factorArray = []
    primeList = []
    for n in range(2,MaxNum):
        if(isPrime(n)):
            primeList.append(n)
    for prime in primeList:
        multiCheck = prime
        while(multiCheck < MaxNum):
            factorArray.append(prime)
            multiCheck = multiCheck * prime
    finalNumber = 1
    for factor in factorArray:
        finalNumber = finalNumber * factor
    return finalNumber
            









def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
