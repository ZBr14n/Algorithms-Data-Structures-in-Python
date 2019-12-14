# -*- coding: utf-8 -*-
"""
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
"""

def countDigits(n=1213234546):
    ct=0
    while True:
        
        n//=10
        ct+=1
        print(n)
        if n <= 0:
            break
    
    print(ct)
    
    #print((121//10)//10)


countDigits()