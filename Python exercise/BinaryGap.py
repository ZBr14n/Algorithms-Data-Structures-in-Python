# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 23:26:08 2019

@author: Brian

Ex.  1001 --> binary gap of length 2 (count the 0s)
     1000010001 --> contains 2 binary gaps (one of length 4 and one of length 3)
     -needs a 1 at the end to count as a "gap"
     
     -scan the string and count the zero's
     -find the index of the one's
     -once the length of the zero's have been found, 
           insert the one's into string at the apprpriate index.
           
"""

def DecToBinary(N):
    
    binary = bin(N)[2:]
    length = len(binary)
    zeros = 0
    for i in range(0,length):
        if binary[i] == "0":
            return binary.count("0",0,length)
        

print(DecToBinary(42))


 
    
        
   # print(countZero)
        
    #returns length of longest binary gap
    
    #returns 0 if N doesn't contain a binary gap
    

#solution(9)