# Jordan Callero
# Project Euler
# February 10, 2016

# This function will find the n'th prime number

def nPrime(n):
    primeCount = 0
    currentNumber = 1
    while(primeCount < n):
        currentNumber += 1
        if(isPrime(currentNumber)):
            primeCount += 1
        

    return currentNumber











def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
