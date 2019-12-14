"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once 
and return the new length.
[0,0,1,1,1,2,2] => [0,1,2] => length = 3

1. loop the list
2. if current elem is the same as the next elem, do nothing.
3. if it is not the same, add 1 to the count.
"""

def removeDuplicates(nums = [1,1,2]):
    ct=1
    for i in range(len(nums)-1):
        if nums[i]!=nums[i+1]:
            ct+=1
    
    return ct

print(removeDuplicates())




