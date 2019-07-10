# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 23:38:28 2019

@author: brlam
"""


def solution(S):
    occurrences = [0] * 26
    
    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1
    
    best_char = 'a'
    best_res = 0
    #the loop has to start at 1 because we need to use index 0 
    for i in range(1, 26):
    #if the count is greater than 0, do this below:
        if occurrences[i] > best_res:
            best_char = chr(ord('a') + i)
            best_res = occurrences[i]
    
    return best_char
    #return best_res



print(solution(S="heello"))