# -*- coding: utf-8 -*-
"""
count the number of 1's and then say that number
1 is "one 1"
2 is "one 2"
3 is "one 3"
11 is "two 1s"  , 

"""

def longestCommonPrefix(arr=["flower","flow","flight"]):
    #all three elements need to have a prefix.
    #use hash table; keys as each char of arr[0], incr. value by 1
    #for each matching char from other arr elements.    
    
    arr=sorted(arr)
    print(arr)
    
longestCommonPrefix()