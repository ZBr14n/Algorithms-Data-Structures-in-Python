# -*- coding: utf-8 -*-
"""
Spyder Editor

"""


def factorial(n):
    
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
        

#print(factorial(5))




"""
This is a temporary script file.
0, 1, 2, 3, 4, 5, 6,  7,  8, 9      --->index of each fib sequence
0, 1, 1, 2, 3, 5, 8, 13, 21, 34     --->actual value from the index

"""
#calculates the fibonacci sequence using recursion (bottoms-up approach)
def bottomsUpFib(n):
     
    if n < 2:
        return n
    else:
        return bottomsUpFib(n-1) + bottomsUpFib(n-2)

#print(bottomsUpFib(5))
    


#top-down approach
def topDownFib