# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:03:19 2019

@author: Brian
- D is distance
- return minimal # of jumps from  x >= y
"""

#let x=10
#  x must be equal or greater than 85 , count minimal of jumps.
def solution(X, Y, D):
    jumps=0
    while True:
        X += D
        jumps+=1
        if X >= Y:        
            break    


    return jumps



print(solution(10,85,30))



#def oddNumbers(l, r):
#
#    for i in range(l,r+1):
#        if i%2 != 0:
#            print(i)
#
#
#oddNumbers(2,9)



#def isElementPresent(A,k):    
#    
#    for i in A:
#        
#        if k == i:
#            print("YES")            
#            break
#        
#    else:
#        print("NO")
#
#
#A = [1,2,3,4,5]     
#isElementPresent(A,2)