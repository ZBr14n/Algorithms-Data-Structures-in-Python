# -*- coding: utf-8 -*-
"""
Created on Sat May 25 09:19:00 2019

@author: brlam
"""


#A=8,B=12           A=54,B=24     A=56,B=42   A=4,B=6)
def gcd(A=54,B=24):
    count=0
    store=0
    while count <= A or count <= B:
        count+=1
        if (A%count)==0 and (B%count)==0:
            store=count
    
    return store
    

#gcd()
#print(gcd())
    

def gcd(A,B):
    if A <= 1 and B <= 1:
        return 1
    else:
        gcd
        
        
        
        
        
        