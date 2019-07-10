# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:28:49 2019

If other nums comes before 1, skip these
 

1. How to determine if 3 should be counted?
As the array loops, insert num to new array
"""

#[2,1,4,3,5]
def Solution():
    A=[2,1,4,3,5]
    #A=[2,1,3,5,4]
    #A=[1,3,4,2,5]
    #A=[2,3,4,1,5]    
    mini=min(A)
    maxi=max(A)
    count=0
    store=[]
    
    if A.index(maxi)==len(A)-1:
        count+=1
    
    
    for i in A:
#        if A.index(i) < A.index(mini) and i > mini:
#            count+=1
#            break
#        if A.index(mini) < A.index(i) < A.index(maxi):
#            if A.index(mini+1) > A.index(i):
#                count+=1
        if i not in store:
            store.append(i)
            if mini+1==i
            
   # print(count)
    print(store)

Solution()