# Jordan Callero
# Project Euler
# February 12, 2016

# This will give the sum of all the primes up the the number N

def sumPrimes(n):

    Sum = 0
    for i in range(2,n):
        if(isPrime(i)):
            Sum += i

    return Sum
        













def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
