# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:17:23 2019

@author: Brian
-every time when there is a match, put them into the array
-How to determine if there is a match??? iterate 2 steps, but then start at 0 and 1
-if paired, do not count it anymore

-line the pairs next to other pairs.
-if the last element does not have a pair, thats the odd occurrence.
"""

#check if count is even
#def isEven(count):

def solution(A):     
    store = []
    A = sorted(A)
    if len(A) == 1:
        store.append(A[0])
    
    print(A)
    for i in range(0,len(A)-1,2):        
        if A[i] != A[i+1]:
            store.append(A[i])
        if len(A) == i+1:
            store.append(A[i])
    
    
    print(store)

A = [9,3,9,3,9,7,9]
solution(A)