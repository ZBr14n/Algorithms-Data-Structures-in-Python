# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 01:06:19 2019

@author: Brian
Write a function that determines if two strings are anagrams.

"""

def areAnagrams(s1,s2):
    
    #count each unique chars in the strings
    #group them side by side 
    x="Eleven plus two" 
    y="Twelve plus one"
    
    
    x=x.lower()
    x=x.replace(" ","")
    
    #designate a count for each unique char; make sure to reset the count back to 0 if its a new char.
    count=0
    i=0
    while True:
        if x[i] in x and x[i]=="e":
            count+=1
        i+=1
        
        if len(x)-1==i:
            break
    
    
    print(count)
    
    
areAnagrams("","")