#!/usr/bin/python3
# Jordan Callero
# Project Euler #2
# February 1, 2016



def EvenFibAdd(MaxLimit):
    Total = 2
    FibNum = 2
    FirstNum = 1
    SecondNum = 2
    ThirdNum = 1
    while(SecondNum < MaxLimit):
        FibNum = FibNum + 1
        ThirdNum = SecondNum + FirstNum
        if(ThirdNum % 2 == 0):
            Total = Total + ThirdNum
            print ThirdNum
        FirstNum = SecondNum
        SecondNum = ThirdNum
    return Total
