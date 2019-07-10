# -*- coding: utf-8 -*-
"""
Created on Wed May  1 07:50:26 2019

@author: Brian
the goal is to rotate the string, K number of times.
if [1,2,3] and rotate 2 times -->       [3,1,2] --> [2,3,1]

challenge: shift the index without messing up the order of the element
-grab current index of each element and add K to it.
-make sure to check that the array is not out of range when shifting elmeents
i+K means the exact index for the current element
-the last element always need to come back to the first index
"""


#[-d:]  means to print the previous index before index 0.
#[:-d]  means to print all the elements excluding the last index
def rotLeft(A, d):    
    return A[-d:] + A[:-d]
  #return A[:-d] + A[-d:]


A = [3, 8, 9, 7, 6]
#rotLeft(A,2)
print(rotLeft(A, 1))

 