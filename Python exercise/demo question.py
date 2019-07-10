# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:26:03 2019

@author: brlam

My notes:
    if given [-1, 0, 4, 5] return 1
        - loop through the array
        - use the count in the loop to check through any missing numbers that are skipped.
        - if count does NOT contain the same number in array, store missing number in array
        - once all the missing numbers in the array is known, we return the lowest number
        
[1, 3, 6, 4, 1, 2]

    

This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer 
(greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
nums = [3, 6, 4, 1, 2]

def solution(nums):
    # write your code in Python 3.6
    sortedList = sorted(nums)
    
    for i in range(len(sortedList)-1):
        #if current element is equal to the next element    [1, 2, 3, 4, 6]
                #for each element, increment by 1
                #
        sortedList[i]+=1
        if sortedList[i] == sortedList[i+1]:
            print(sortedList[i])
        else:
            sortedList[i+1] += 1
            print(sortedList[i])
            
solution(nums)            

















