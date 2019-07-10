# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:06:14 2019

@author: brlam
 if string[i] != string[i+1]:
                isCharUnique=True
                if isCharUnique==True:
                    print(string[i],end=' ')
            else:
                pass
            break
"""

#using an array 
def isUnique(string):
    arr = []
    for i in string:
        if i not in arr:
            arr.append(i)
            
    
    for j in arr:
        print(j,end=' ')            
        


#data structure     
def isUnique2(string):

    isCharUnique = False   
    for i in range(len(string)):
        for j in range(i+1,len(string)):            
            if string[i] == string[j]:
                return isCharUnique   #false when there is duplicates
    
    return True    #returns true if all unique chars        
                



def isUnique3(string):
    string = sorted(string)
    print(string)
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            
            print(string[i],end=' ')
        
#isUnique("enumerate")
#isUnique2("apple")
isUnique3("tendinitis")
#isUnique2("google")
#isUnique2("tendinitis")
#isUnique2("westermann")



 
