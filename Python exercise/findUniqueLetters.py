# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#if same chars, copy the letter one time (use break)


def findUniqueLetters(input="aaaccbbba"):
    
    emptyString = ""
    
    for i in range(0,len(input),1):
        #if its not already in the string stored string, add it
        
        if input[i] != emptyString:
            emptyString += input[i]
        
        #after appending the unique character,
        #we need to scan it again, to see if the char is
        #reoccuring.         
        for j in range(0,len(emptyString),1):
            print(emptyString[j])
        
        
   # print(emptyString)
    
    

findUniqueLetters()