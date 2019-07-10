# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 19:15:54 2019

@author: brlam
"""

def IsomorphicStrings(s="paper",t="title"):
    
    #preserve the order; in other words, 
    #if one has two of the same chars, the other str needs the same

#    
#    
    for i,j in zip(s,t):
      #  print(s.index(i),t.index(j))
        if s.index(i)!=t.index(j):
            return False
    else:
        return True
    
#IsomorphicStrings()
print(IsomorphicStrings())        
    