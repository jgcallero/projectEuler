# Jordan Callero
# Project Euler
# February 10, 2016

# This progam will take a number n and see if there is a
# Pythagrian triplet where a+b+c=1000

import math

def PythagTriple(targetNumber):
    for a in range(1,int(targetNumber/2)):
        for b in range(1,int(targetNumber/2)):   
            c = float(a**2+b**2)**.5
            if(a+b+c == targetNumber):
                return [a,b,c]
                
