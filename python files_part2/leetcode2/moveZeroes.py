"""
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

two pointer method:
1. scan arr; for each non-zero elem,  assign this to aux, and then set it to 0
2. After setting it to 0, we can incr. pointer i
3. Once we set it to 0, and set the first element to equal aux, we can move on.


push/pop method:
1. Assign orig. length of array to variable.
2. For each 0 that we pop out of the array, subtract Orig. Length of arr by 1.
3. If i is equal to this length, we stop since it would be the last element of the old array.

edge case
[1,2,3,0,1]
"""

def moveZeros(nums):
    oldLen = len(nums)
    
    for i in range(len(nums)):
        
        if 0 in nums:
            nums.pop(i)
            print(nums)
            nums.append(0)
        if i==oldLen:
            print('hi')
            break
    print(nums)            
                
moveZeros([0,1,0,3,12])