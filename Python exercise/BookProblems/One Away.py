# -*- coding: utf-8 -*-
"""
Created on Sat May 25 06:12:33 2019

@author: Brian
returns the length of the longest word from the string that is a valid password
S = "test 5 a0A pass007 ?xy1"
    1.scan string
    2.count the length
    3.isAlpha or isDigit - test for letter evens and odd digits
    
"""

s1 = "test 5 a0A pass007 ?xy1"
s2="pass007"

for i in range(len(s2)):
    if ord(s2[i]) < 97 or ord(s2[i]) > 122:
        print(s2[i])