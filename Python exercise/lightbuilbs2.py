# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 22:28:47 2019

@author: Brian
1. How to determine if 3 should be counted?
Essentially, as we loop thru each num, we store num in tmp array
Every next num, we check if it equals tmp array by subtracting 1.
If it equals num-1, incr. count+=1


scan the array
if first num is not mini, then store it to tmp
if next num is mini, incr. count+=1
At next num, compare num with tmp, if num-1 is not equal, store into tmp
At next num(3), if num-1 in tmp, incr count+=1
"""

def Solution():
    #output 3
    #A=[2,1,4,3,5]
    
    #A=[2,1,3,5,4]
    A=[1,3,4,2,5]
    #A=[2,3,4,1,5]  
    
    store=[]
    mini=min(A)
    for i in A:
        if i not in store:
            store.append(i)
            if (i-mini or i+mini) in store:
                print(i)

    
    
Solution()