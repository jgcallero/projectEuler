# Jordan Calero
# Project Euler
# February 25, 2016

# This function will take a pyramid of numbers and find the
# largest numbe taken by adding the numbers through the path
# The filename will be "Pyramid.txt"


def pyramidPath():

    pyramid = pyramidRead()

    print(pyramid)

    for i in range(len(pyramid)-2,-1,-1):
        for j in range(i,-1,-1):
            print(pyramid[i][j],pyramid[i+1][j],pyramid[i+1][j+1])
            if(pyramid[i+1][j] > pyramid[i+1][j+1]):
                pyramid[i][j] = pyramid[i+1][j] + pyramid[i][j]
            else:
                pyramid[i][j] = pyramid[i+1][j+1] + pyramid[i][j]

    return pyramid[0][0]






def pyramidRead():
    pyramidFile = open("Pyramid.txt", 'r')
    pyramidArray = []
    for i in pyramidFile:
        pyramidArray.append(i.strip('\n').split())


    for i in range(len(pyramidArray)):
        for j in (range(i+1)):
            pyramidArray[i][j] = int(pyramidArray[i][j])

    return pyramidArray
