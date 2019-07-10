# -*- coding: utf-8 -*-
"""
Created on Fri May  3 19:41:09 2019

@author: Brian
"Design an algorithm to compute the nth ..:; 
"Write code to list the frst n .. 
"Implement a method to compute all..:; and so on.

     1, 5, 10, 25
     calculate the number of ways of representing n cents    

-use recursion to keep dividing by 5 until it reaches 1.
     
"""

def ReduceCents(n):
    
    if n == 0:
        return n
    else:         
        print(str(n-1) + " hello")
        ReduceCents(n-1)
    
ReduceCents(10)