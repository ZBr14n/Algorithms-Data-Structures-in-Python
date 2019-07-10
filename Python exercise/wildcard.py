# -*- coding: utf-8 -*-
"""
Created on Tue May  7 09:37:26 2019

@author: brlam
"""

def solution(words,query):
 
    store = []
    bestMatch = 0
    for x in query:
        for y in words:
            if len(y)==len(query):
                if x in y:
                    store.append(y)            
            else:
                print("no match")
                

    bestMatch = len(store)-1
    return store[bestMatch]
        
print(solution(['foo','baz','bar'],"b*z"))
#solution(['foo','baz','bar'],"b*r")