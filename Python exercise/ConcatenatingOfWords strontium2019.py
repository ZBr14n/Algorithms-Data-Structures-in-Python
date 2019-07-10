# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:08:09 2019

@author: brlam
1.check to see if each word ending is MATCHED with the other words' ending chars
2.merge each string in the array as one string
3. 

words[1] + words[0] + words[2] = "aaaaaabbbbab". 
The longest substring is composed of letter 'a' and its length is 6.
"""

isMatched=False
words=["aabb", "aaaa", "bbab"]


for i,x in enumerate(words):
    print(i,x)