#Jordan Callero
#Project Euler
#February 22, 2016

#This program will take the numbers in NumberFile.txt and add them,
#Returning the total

def addBigNumbers():

    numberFile = open("NumberFile.txt", 'r')
    total = 0
    for i in numberFile:
        print(i)
        total += int(i)

    return total
