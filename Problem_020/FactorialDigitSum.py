# Jordan Callero
# Project Euler
# April 20, 2016

# Takes a number and takes it's factorial, and adds the digits
import math


def FactorialDigitSum(num):
    factorial = math.factorial(num)
    stringFact = str(factorial)
    total = 0
    for i in range(len(stringFact)):
        total += int(stringFact[i])

    return total
