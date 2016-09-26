# Jordan Callero
# Project Euler
# February 10, 2016

# This Function will take the file "NumberList.txt", and an integer,
# And return the highest number you can get by multiplying the
# n adjacent numbers together.

def LargestProductSeries(Length):

    masterNumberArray = readFile()
    testNumberArray = []
    for i in range(0,Length):
        testNumberArray.append(masterNumberArray[i])

    maxNumber = long(MultiplyList(testNumberArray))
    for i in range(Length,len(masterNumberArray)):
        ShiftList(testNumberArray, masterNumberArray[i])
        print maxNumber
        if(MultiplyList(testNumberArray) > maxNumber):
            maxNumber = long(MultiplyList(testNumberArray))

    return maxNumber
        








def readFile():
    numberFile = open('NumberList.txt', 'r')
    List = ((numberFile.read()).replace('\n',''))
    numArray = []
    for i in List:
        numArray.append(int(i))
        
    return numArray


def MultiplyList(List):
    total = long(1)
    for i in List:
        total *= i
    return total

def ShiftList(List, newElement):
    for i in range(len(List) - 1):
        List[i] = List[i+1]
    List[-1] = newElement
    
        
