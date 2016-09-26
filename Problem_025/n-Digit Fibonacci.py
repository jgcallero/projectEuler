# Jordan Callero
# Project Euler
# May 6, 2016

# This program will find the first fibonacci number with n digits

def nFib(n):
    fib1 = 1
    fib2 = 1
    fib3 = 2
    index = 3
    while(len(str(fib3)) < n):
        temp = fib2 + fib3
        fib1 = fib2
        fib2 = fib3
        fib3 = temp
        index += 1
    return index
    
