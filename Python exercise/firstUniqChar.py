# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:44:52 2019

@author: brlam
"""

#minimum requirement is to scan thru the for loop 


def firstUniqChar(s="loveleetcode"):
    
    store={}
    for i,j in enumerate(s):
        store[j]=store.get(j,0)+1
    
    print(store)
    
    list=[k for k in store.values()]
    print(list)
    for v in s:
        if store[v]==1:
            return s.index(v)
    else:
        return -1
    

    

print(firstUniqChar())
#firstUniqChar()