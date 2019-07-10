# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 19:42:58 2019

@author: Brian

[6,11]

6%6==0
7%6
8%6
"""

def CountDiv(A,B,K):
    count=0
    while A <= B:
        if A%K==0:
            #print(A)
            count+=1
        
        A+=1
    
    
    print(count)
    
    
CountDiv(6,11,2)