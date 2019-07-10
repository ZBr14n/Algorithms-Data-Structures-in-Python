# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:34:52 2019

@author: Brian
"""

def solution(A):
    A = sorted(A)
    plus1 = 1
    i=0
    
    for i in A:
        i+=1
        if i in A:
            pass   #we don't want to print unwanted numbers at output
        else:
            return i

#A=[2,3,1,5]
A=[12,16,14,13]
print(solution(A))    