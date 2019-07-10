# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:48:46 2019

@author: brlam
Input: 3
Output: ( ( () ) ) ,
        ( () () ) , 
        ( () ) () , 
        () ( () ) , 
        () () ()
"""

def recurse(n):
    string=""
    count=0
    
    if string == "()()()" or n==0:
        return string
    else:
        string.join("(")
        if len(string)==n:
            string.join(")")
            count+=1
        if count!=n:
            recurse(n-1)
        
    return string


print(recurse(3))





#def recurse(n):
#    
#    if n < 1:
#        return n
#    else:
#        print(n-1)
#        recurse(n-1)


#recurse(10)
