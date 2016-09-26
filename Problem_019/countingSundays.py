# Jordan Callero
# Project Euler
# April, 20, 2016

# This program will count the number of sundays that fell
# On the first of the month from 1 Jan 1901 to 31 Dec 2000.

def firstMonthCount():
    monthArray = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dayOfWeek = 2
    sundayStart = 0

    for year in range(1,101):
        for month in range(12):
            
            if(month == 1):
                if((year % 4 == 0)):
                    dayOfWeek += 1

            dayOfWeek = (dayOfWeek + monthArray[month])
            
            if(dayOfWeek % 7 == 0):
                sundayStart += 1
                
    return sundayStart
