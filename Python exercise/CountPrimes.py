# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:37:01 2019

@author: Brian
"""


def isPrime(num=10):
    #if num can only be divided evenly by 1 or by itself.
    #if num%i!=0
    
    for i in range(1,num+1):
        if num%i==0:
            print(i)
            
            
isPrime()






#def CountPrimes(Input=20):
#    #what is a prime? Prime is num that is a multiply by 1 or itself
#    ct=0
#    for i in range(1,Input+1):
#        #print(i,Input%i)
#        print(i,Input/i)
#        
#    
#    
#    
#    
#CountPrimes()