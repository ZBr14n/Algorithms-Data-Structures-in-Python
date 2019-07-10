# -*- coding: utf-8 -*-
"""
Created on Sat May 25 09:19:23 2019

@author: brlam
Smallest substring of all characters

input:  arr = ['x','y','z'], str = "xyyzyzyx"
output: "zyx"

logc: create a dictionary. Store the string into the dict and loop it
remove chars that do not fit in to arr as the loop runs.
-if store is in arr, increment by 1 for that index.
-use dict keys to represent the count
"""

def getShortestUniqueSubstring(arr=['x','y','z'],string="xyyzyzyx"):
    store={}
    for k in range(len(string)):
        store[k]=string[k]
        
    print(store)
    
    
    
    
    
    
    
    

    
    
#    store = {}
#    count=0
#    for i in range(len(string)):
#        if string[i] in arr:
#            count+=1
#        store[count,i]=string[i]
#        
#    print(store)
#        
        
    #return ""
    
    
getShortestUniqueSubstring()