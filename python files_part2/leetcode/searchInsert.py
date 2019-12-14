"""
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

goal:
1. return index if target is found
2. if target is not found, return the index where it supposed to be. 

1. loop thru the arr
2. check if target is within nums, if so return the index i
3. If target is not found, compare the next number that is greater than the target.
   Subtract that index by 1 to find where the target index should be in. 

2 or 7
"""

def searchInsert(nums=[1,3,5,6],target=0):
    if target in nums:
        print(nums.index(target))
    else:
        for i,j in enumerate(nums):            
            if j > target: 
                #add 1 to the end because the for loop started at 0. 
                return (i-1)+1
        else:
            return len(nums)

# searchInsert()
print(searchInsert())