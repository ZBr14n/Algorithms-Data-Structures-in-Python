# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:12:06 2019

@author: brlam

Check Permutation: Given two strings, 
write a method to decide if one is a 
permutation of the other
"""

#def solution(s1,s2):
#    if len(s1) == len(s2):
#    
#    else:
#        


def occur(S): 
    occurrences = [0] * 26
    
    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')]+=1
        
    
    for x in occurrences:
        print(x,end=' ')
    
occur("gzzks")    