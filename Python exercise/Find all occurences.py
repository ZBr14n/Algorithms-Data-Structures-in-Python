# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 08:41:14 2019

@author: brlam
"""

#for i in range(1,4):  #rows
#    for j in range(1,3):#columns
#        print(i*j,end=' ')
#    
#    print("\n")




def solution(S):
    occurrences = [0] * 26

    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1

    best_char = 'a'
    best_res = 0

    for i in range(1, 26):
        if occurrences[i] >= best_res:
            best_char = chr(ord('a') + i)
            best_res = occurrences[i]

    return best_char




print(solution("geeksforgeeks"))