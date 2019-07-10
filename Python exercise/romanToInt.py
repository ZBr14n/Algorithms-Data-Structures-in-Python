# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 15:37:54 2019

@author: brlam
1000 + (100-1000) = 1000+900 = 1900
"""

def romanToInt(s="MCM"):

    roman={
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    

    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z += roman[s[i]]-roman[s[i+1]]
        else:
            z = roman[s[i]]+roman[s[i+1]]
            
    return z


print(romanToInt())        