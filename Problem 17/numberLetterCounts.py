# Jordan Callero
# Project Euler
# February 24, 2016

# This function will take any number below 1000 and add up all the
# English letters used to write all of the numbers up to that number

numberDictionary = {
        1    : "one",
        2    : "two",
        3    : "three",
        4    : "four",
        5    : "five",
        6    : "six",
        7    : "seven",
        8    : "eight",
        9    : "nine",
        10   : "ten",
        11   : "eleven",
        12   : "twelve",
        13   : "thirteen",
        14   : "fourteen",
        15   : "fifteen",
        16   : "sixteen",
        17   : "seventeen",
        18   : "eighteen",
        19   : "nineteen",
        20   : "twenty",
        30   : "thirty",
        40   : "forty",
        50   : "fifty",
        60   : "sixty",
        70   : "seventy",
        80   : "eighty",
        90   : "ninety",
        100  : "hundred",
        1000 : "thousand"
        }


def numberLetterCount(maxNum):


    totalLetters = 0

    for i in range(1, maxNum+1):
        totalLetters += numberTranslate(i)
    
    return totalLetters

def numberTranslate(i):
    numberWord = ""
    if(i <= 100):
        if(i < 20):
            numberWord = numberDictionary[i]
            print(numberWord, len(numberWord.strip())) 
            return len(numberWord.strip())
        else:
            stringI = list(str(i))
            magnitude = len(stringI) - 1
            for i in stringI:
                j = int(int(i) * (10 ** magnitude))
                if(j != 0):
                    if (magnitude >= 1):
                        if(magnitude == 1):
                            numberWord += numberDictionary[j]
                        else:
                            numberWord += numberDictionary[int(i)] + numberDictionary[j]
                    else:
                        numberWord += numberDictionary[j]
                magnitude -= 1

            print(numberWord, len(numberWord))         
            return len(numberWord)

    else:
        stringI = list(str(i))
        magnitude = len(stringI) - 1
        if(stringI[-2] == '1'):
            stringI[-2:] = [''.join(stringI[-2:])]
        for i in stringI:
            if(i != '0'):
                if (int(i) < 20 and int(i) >= 10):
                    numberWord += "and" + numberDictionary[int(i)]
                elif (magnitude >= 1):
                    if(magnitude == 1):
                        j = 10 * int(i)
                        numberWord += "and" + numberDictionary[j]
                    else:
                        j = 10 ** magnitude
                        numberWord += numberDictionary[int(i)] + numberDictionary[j]
                else:
                    if "and" not in numberWord:
                        j = int(int(i) * (10 ** magnitude))
                        numberWord += "and" + numberDictionary[j]
                    else:
                        j = int(int(i) * (10 ** magnitude))
                        numberWord += numberDictionary[j]
            magnitude -= 1

        print(numberWord, len(numberWord)) 
        return len((numberWord))


            
        
        
