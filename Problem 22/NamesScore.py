# Jordan Callero
# Project Euler
# April 22, 2016

# This will take a list of names in names.txt, all on one line,
# all names in "" and seperated by , and then organize them by name
# Then add up the letters and multiply the total by their point in
# The list

letterDictionary = {
    'A' : 1  ,
    'B' : 2  ,
    'C' : 3  ,
    'D' : 4  ,
    'E' : 5  ,
    'F' : 6  ,
    'G' : 7  ,
    'H' : 8  ,
    'I' : 9  ,
    'J' : 10  ,
    'K' : 11  ,
    'L' : 12  ,
    'M' : 13  ,
    'N' : 14  ,
    'O' : 15  ,
    'P' : 16  ,
    'Q' : 17  ,
    'R' : 18  ,
    'S' : 19  ,
    'T' : 20  ,
    'U' : 21  ,
    'V' : 22  ,
    'W' : 23  ,
    'X' : 24  ,
    'Y' : 25  ,
    'Z' : 26
    }

def nameScore():
    nameList = nameRead()
    total = 0
    listNum = 1
    for i in nameList:
        nameTotal = 0
        for j in i:
            nameTotal += letterDictionary[j]
        total += nameTotal * listNum
        listNum += 1
    return total







def nameRead():
    nameFile = open("names.txt", 'r')
    nameArray = []
    nameString = nameFile.read().split(',')
    for i in nameString:
        nameArray.append(i.strip('"'))
    return sorted(nameArray)
