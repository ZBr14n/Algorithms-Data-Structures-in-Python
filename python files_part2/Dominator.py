# -*- coding: utf-8 -*-
"""
 given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.
"""

def findMode():
    
    A=[3,4,3,2,3,-1,3,3]
    
    #determine the mode of array, that covers more
    #than half of the arr
    ht={}
    size=len(A)//2
    for i,j in enumerate(A):
        ht[j]=ht.get(j,0)+1
        if ht.get(j,0)+1 > size:
            return j
        
        
    return 0


def solution():
    
    A=[3,4,3,2,3,-1,3,3]
    x=findMode()
    for i in range(len(A)):
        if x==A[i]:
            print(i)


solution()

#print(solution())





