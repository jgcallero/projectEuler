# Jordan Callero
# Project Euler #6
# February 3, 2016

# This function will take a number, and return the Sum square difference
# Between them

def sumSquareDifference(N):
    sumofSquares = 0
    for n in range(1,N+1):
        sumofSquares = sumofSquares + (n*n)

    sumofDigits = 0
    for n in range(1,N+1):
        sumofDigits = sumofDigits + n

    squareofSum = sumofDigits*sumofDigits
    return(squareofSum - sumofSquares)
