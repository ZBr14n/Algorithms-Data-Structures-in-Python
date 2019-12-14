"""
Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

1. Since the array is sorted, we can check if [i] and [i+1] are the same nums or not. 
If there is a repeat, we only want one element of it; discard the rest.
2. Set other elements to null, and keep the running count of unique elements.   
[i+1]
"""
# [0,0,0,1,1,2,2,2]
# [1,1,2]
def removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]):
    ct=0
    for i in range(len(nums)-1):        
        if nums[i]!=nums[i+1]:            
            ct+=2
    
    return ct
            
print(removeDuplicates())


            