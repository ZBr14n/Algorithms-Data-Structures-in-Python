# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:53:23 2019

@author: brlam


aabcccccaaa --> a2blc5a3
#Input2 = "aabcccccaaa"     aaabbc
-How do you count how many repeated characters there are in a string?
-No need to determine if the string is unique or not.
"""

#aa aa ab bb bc
def countRepeats():    
    Input = "aabcccccaaa"    
    k=0
    count=0
    tempString = ""
    sum=0
    for i in range(len(Input)):
        count+=1    
                
        if i+1 >= len(Input) or Input[i]!=Input[i+1]:
        #scan until chars dont match, return length to new string
            tempString+=Input[i]+str(count)
        #reset the count after finding the length of each char
            count=0
        
        
    print(tempString)
    #return tempString if len(tempString) < len(Input) else Input



#print(countRepeats())
countRepeats()            
    
     






