# -*- coding: utf-8 -*-
"""
Created on Fri May 31 02:10:29 2019

@author: Brian
Goal:  return smallest positive integer (greater than 0)
1. if nums are all negative integers, then return 1
2. if nums are unsorted, sort them first;
find the lowest positive integer in the sorted array, 
and add 1 to it; if its not equal to next num, then use it. 
If equal, go to the next num and do the same thing.
"""

def findMin(A,mini):
    for j,k in enumerate(A):
        mini+=1
        if mini != A[j+1]:
            return mini
        else:
            continue
    
    return "fail"
    

def MissingInteger(A = [1, 3, 6, 4, 1, 2]):
    A=sorted(A)
    for i in A:
        if i < 0:
            return 1
    
    
    print(findMin(A,min(A)))
    
    

MissingInteger()