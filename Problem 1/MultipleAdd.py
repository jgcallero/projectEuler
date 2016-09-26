#!/usr/bin/python3
# Jordan Callero
# Project Euler #1
# February 1, 2016

# Code will have input of list of numbers, and max bound, then
# The function will return all numbers that are divisble by at least
# One of the numbers in the list

def MultiAdd(factorList, MaxLimit):
    factorCheck = False
    currentNumber = 1
    addTotal = 0
    while(currentNumber < MaxLimit):
        factorCheck = False
        arrayIndex = 0
        while(not factorCheck and arrayIndex < len(factorList)):
            if(currentNumber % factorList[arrayIndex] == 0):
                addTotal = addTotal + currentNumber
                factorCheck = True
            arrayIndex = arrayIndex + 1
        currentNumber = currentNumber + 1
    return addTotal
