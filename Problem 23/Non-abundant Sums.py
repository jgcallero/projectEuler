# Jordan Callero
# Project Euler
# May 4, 2016

# This function will sum all of the positive integers which
# can not be written as the sum of two abudant numbers.

# Note: An abundant number is a number where the factors added
#  together is larger than the number itself.


def nonAbuSum():
    abudantList = abuList()
    abudantAddList = abuAdd(abudantList)
    total = 0
    for i in range(1, 28123):
        if (i not in abudantAddList):
            total += i
    return total





def abuList():
    AbudantList = []
    for i in range(1,28123):
        factorList = (factors(i))
        factorSum = 0
        for factor in factorList:
            if(i != factor):
                factorSum += factor
        if(i < factorSum):
            AbudantList.append(i)
    return AbudantList
            



def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def abuAdd(abudantList):
    abuAddlist = []
    for i in abudantList:
        for j in abudantList:
            #if(i+j not in abuAddlist):
                abuAddlist.append(i+j)
    return set(abuAddlist)               
