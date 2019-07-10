# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 18:16:03 2019

@author: Brian

One of the things that is tricky about this problem is that:
if {8,1} then the answer is 8.
if {8,1,1,1} then the answer is 8.
If {8,1,1,1,1,1,2} then it is 9


1. calculate highest number (height) from the input array
2. 
"""
# =============================================================================
    #arr[] = {5,3,6,9}...output 9.
    #to find the highest number, you have to cycle thru the array.
    #declare temp variable and store each value from the array as it cycles thru
    #change to new  value ONLY IF it is greater than the current value being compared
    #if not, do nothing and keep moving on until the array loop ends.
# =============================================================================
nums = [8,1,1,2]  
def findTallestHeight(inputArray):
    #given an array, find the highest number.    
    storeTemp=0
    for i in range(len(inputArray)):        
        if inputArray[i] > storeTemp:
            storeTemp = inputArray[i]

            
    return storeTemp



#[8,1,1,2]  
# =============================================================================
#            if not isTaller and inputArray[k] >= (j+1):
#                countStrokes+=1
#                isTaller = True
#            else:
#                if isTaller and inputArray[k] < (j+1):
#                    isTaller = False

# After finding out the height, let the height represent the rows of the skyline
# 1. create a for loop that loops from 0 to whatever the height is. (loop thru each rows represent as the height of the skyline)
#                                                                   (loop thru each column represent as the length of the skyline in total)          
# 2. count row 1 immediately (the base of thhe skyline)
# 3. #check to see if next column has a "gap", if so increment the current count.     

# =============================================================================
def findMinimumStrokes(inputArray):
    countStrokes = 0
    
    #toggle boolean to True only if column is higher than the other when comparing.
    for j in range(findTallestHeight(inputArray)):   #rows
        isTaller=False   
        for k in range(len(inputArray)):             #columns
           # compare current column and next column    nums = [8,9]
           if not isTaller and inputArray[k] >= j:
                countStrokes+=1                
                isTaller = True  
           else:
                if isTaller and inputArray[k] < j:
                    isTaller = False
    
    
    
    if countStrokes > 1000000000:
        return -1
    else:
        return countStrokes





print(findMinimumStrokes(nums))









  