# Jordan Callero
# Project Euler
# February 24, 2016

# This function will take a number, and add up all the
# individual digits

def powerDigitSum(number):
    stringNum = str(number)
    total = 0
    for i in stringNum:
        total += int(i)
    return total
