# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:54:56 2019

@author: brlam
range(len(input),-1,-1):
    print(input[i],end='')

#            print(storeBase2[j],end='')
#        else:
#            print("None",end='')
    #101100101
"""



#convert from binary string to an integer
def toNum(input):
    #loop thru the length of the string
    storeBase2 = []
    sum=0
    for i in range(0,len(input)):
        storeBase2.append(2**i)
    
    storeBase2.reverse()
    for j in range(0,len(storeBase2)):
        k = j
        if input[k] == "1":
            sum+=storeBase2[j]
    
    return sum

#if num is equal to 2 * n in the for loop, then it is even.
def isEven(num):
    if num%2 == 0:
        return True
        
    
#def isOdd(num):
#    if num%2 != 0:
#        return False

def reduceToZero(num):
    num = toNum(num)   #assign the sum from toNum() to num
    print("Starting number is: " + str(num))
    #if even, divide by 2
    #if odd, subtract 1 
    while True:
        if isEven(num) == True:     #plug num to compute whether it is even or not
            num /= 2
        else:
            num -= 1
        
        print(num)
        
        if num == 0:
            break
        
        
        
#reduceToZero(171)    
reduceToZero("0111")            