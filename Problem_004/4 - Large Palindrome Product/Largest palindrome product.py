#!/usr/bin/python3
# Jordan Callero
# Self Project
# September 21 2015

#
#
#   A palindromic number reads the same both ways.
#   The largest palindrome made from the product of
#   two 2-digit numbers is 9009 = 91 × 99.
#
#   Find the largest palindrome made from the product of two 3-digit numbers.
#
#

def main():

    for i in reversed(range(10)):
        for j in reversed(range(10)):
            for k in reversed(range(10)):
                number = i*100000 + j*10000 + k*1000 + k*100 + j*10 + i
                factorList = factors(number)
                Success = True
                while(len(factorList) > 2 and Success):
                    last = len(factorList)-1
                    while(len(str(factorList[0] * factorList[last])) > 3 and last != 0):
                        last = last - 1
                    if(last == 0):
                        Success = False
                    if(last != 0):
                        newDigit = factorList[0] * factorList[last]
                        del factorList[last]
                        del factorList[0]
                        factorList.append(newDigit)
                        factorList = sorted(factorList)
                if(len(str(factorList[0])) < 4 and len(str(factorList[1])) < 4 and Success):
                    return number    
 
                




def factors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return sorted(primfac)


