"""
Given an array of integers, return indices of the two numbers such that 
they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.


Intuition:
goal: we have to find 2 numbers in the list that make up the target.
As we pass by each elem, we store the difference in the hash table for 
faster retrieval of the other pair 


Store the elem as the key; Store the difference as the value
Check if next number is within the Hash Table that matches the key (The next number MUST equal the DIFFERENCE when checked, otherwise edge cases like 22-11=11 would equal itself and hence the duplicate value);
if so, return the value for that key.

[2, 7, 11, 15], target = 22
[2,7,11,15], 9
"""

class Solution:
    def twoSum(self, nums, target):

        store={}
        for i in range(len(nums)):
            difference = target - nums[i]
            # this will avoid returnning the same value, in the edge case where elem is 11
            if nums[i] not in store.values():
                store[nums[i]] = difference
            else:
                # if the current elem(15) is equal to the difference in store
                # return the corresponding index from nums using the value stored in dictionary
                return [nums.index(difference), i]
            
        # print(store)
                        
# Solution().twoSum([2, 7, 11, 15],22)
print(Solution().twoSum([2,7,11,15],9))        