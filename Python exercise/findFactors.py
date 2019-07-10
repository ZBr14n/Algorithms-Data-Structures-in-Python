# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 07:59:36 2019

@author: Brian
"""


N=50
num=0
for i in range(1,N+1):
    if N%i==0:
        print(int(N/i),end=', ')
        count+=1


print("\nthe count in total is:   " + str(count))        

        