# Jordan Callero
# Project Euler
# February 12 2016

# This program will take an NxN grid, take from NumberGrid.txt and
# look for the largest number it can generate by taking M adjacent
# numbers in the same direction and multiplying them together.


def LargestGridMultiply(adjacentSize):
    numberGrid = readFile()
    largestProduct = 0

    testProduct = lineTest(numberGrid, adjacentSize, 0)
    if(testProduct > largestProduct):
        largestProduct = testProduct

    testProduct = lineTest(numberGrid, adjacentSize, 1)
    if(testProduct > largestProduct):
        largestProduct = testProduct

    testProduct = diagonalLineTest(numberGrid, adjacentSize, 0)
    if(testProduct > largestProduct):
        largestProduct = testProduct

    testProduct = diagonalLineTest(numberGrid, adjacentSize, 1)
    if(testProduct > largestProduct):
        largestProduct = testProduct

    return largestProduct

    

    



def readFile():
    
    numberFile = open('NumberGrid.txt', 'r')
    finalArray = []
    for line in numberFile:
        gridLine = (line.split())
        for i in range(len(gridLine)):
            gridLine[i] = int(gridLine[i])
        finalArray.append(gridLine)
    return finalArray


def lineTest(numberGrid, adjacentSize, lineType):
    largestProduct = 0
    numberArray = []
    for i in range(adjacentSize):
        numberArray.append(0)
    for i in range(len(numberGrid)):
        for j in range(len(numberGrid)-adjacentSize+1):

            if(lineType == 0):
                for k in range(adjacentSize):
                    numberArray[k] = numberGrid[i][j+k]
            if(lineType == 1):
                for k in range(adjacentSize):
                    numberArray[k] = numberGrid[j+k][i]

            testProduct = multiplyArray(numberArray)
            if(testProduct > largestProduct):
                largestProduct = testProduct

    return largestProduct

def diagonalLineTest(numberGrid, adjacentSize, lineType):
    largestProduct = 0
    numberArray = []
    for i in range(adjacentSize):
        numberArray.append(0)
    for i in range(len(numberGrid)-adjacentSize+1):
        for j in range(len(numberGrid)-adjacentSize+1):

            if(lineType == 0):
                for k in range(adjacentSize):
                    numberArray[k] = numberGrid[i+k][j+k]

            if(lineType == 1):
                for k in range(adjacentSize):
                    numberArray[k] = numberGrid[i+adjacentSize-k-1][j+k]

            testProduct = multiplyArray(numberArray)
            if(testProduct > largestProduct):
                largestProduct = testProduct

    return largestProduct
    

     
def multiplyArray(array):
    total= 1
    for i in array:
        total *= i
    return total
