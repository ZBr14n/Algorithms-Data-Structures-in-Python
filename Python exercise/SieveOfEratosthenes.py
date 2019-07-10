# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:33:08 2019

@author: brlam
Sieve of E
n=11

2 4 6 8 10
3 6 9 
4 8 
5 10

"""
import time


def SieveOfEratosthenes(n=51):
    
    store = []
    prd = 0
    for i in range(2,n):
        for j in range(2,n):
            #finds all multiples up to n
            prd = i * j
            #stop the loop when it is larger than n
            if prd > n:
                break
            else:
                #store these multiples into a list to be used for comparison
                store.append(prd)
        
        #use outer loop to find all the primes that are not in the list, and print them out
        #starts at 2...up to n
        if i not in store:
            print(i,end=' ')

    
    
start = time.time()
SieveOfEratosthenes()
end = time.time()
print(end-start)


