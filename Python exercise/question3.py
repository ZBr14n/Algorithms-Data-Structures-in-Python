# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:11:00 2019

@author: Brian

#given a random number, say 48, write that in binary
        1 2 4 8 16 32 64 128 256 512 
"""

def toBinary(num):
    #run from 0-10 with base 2 using  pow() to compute exponents.
    sumExp=0
    storeExponents = []
    tempStore = []

    for i in range(0,10):
        base2Num = pow(2,i)
        storeExponents.append(base2Num)
        #after we store the values into the list, we can run another for loop in it
        #we have to print all the numbers less than num
    for j in range(len(storeExponents)-1,-1,-1):
        if storeExponents[j] < num:            
            sumExp+=storeExponents[j]
            print(sumExp)
                
            
#            if sum != 0:
#                print("1",end='')                
#            else:
#                print("0",end='') 
#                    
#            if sum == num:
#                break
#                        
               
    
toBinary(10)        
        
    
    
    