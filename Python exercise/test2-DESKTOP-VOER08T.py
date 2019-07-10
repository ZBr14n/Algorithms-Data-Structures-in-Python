# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 21:49:30 2019

@author: Brian
1. use while loop==True
2. e.g. 2^10 , incr. count to 10 and then stop.
3. For each count, multiple itself.


what to do if the power is -2?
if -2 takes the abs of it.
2^-2 = 1/2^2
A=[10,14,13,12,15]
A=[2,3,1,5]
"""

def solution(A=[10,14,13,12,15]):
    A=sorted(A)
    k=0
    for i in enumerate(A):
        
        if A[k]+1!=A[k+1]:
            return A[k]+1
            #print(A[k]+1)
            
        k+=1
        
        if k == len(A)-1:
            break


#solution()
print(solution())

        
#
#def myPow(x,n):
#    origN=n
#    count=1
#    
#    if n < 0:
#        n=abs(n)
#    
#    temp=x
#    while True:
#        
#        temp*=x
#        #print(count)
#        
#        count+=1
#        if count==n:
#            break
#        
#    
#    if origN < 0:
#        temp=1/temp
#        
#    print(temp)
#    
#
#myPow(2,-15)

#myPow(2.00000,10)
#myPow(2.10000,3)
#myPow(2.00000,-2)

