"""
Input: numbers = [2,7,11,15], target = 9
13-2=11
We have to store difference that corresp. to index.

dictionary appr:
Think about what the dictionary should return.
ht[diff] = index


Binary Search approach:
Compare whether the split arrays are greater than the target or not. 
We only want the array that is lower than the target.
1. Get the length of the array and dividie it by 2 to get the midpoint (round it)
2. Compare target with a0/...rrays; we choose the array that is less than the target since 
"""

"""
Input: numbers = [2,7,11,15], target = 22
Output: [1,2]

what is binary search? it is searching algorithm that keeps dividing the array into halves
until it finds the number.
"""

# numbers = [2,7,11,15]
# target = 15
"""
-keep splitting the array in half and compare mid with target 
-if mid is less than target, then incr. index to second array. 
"""

nums = [3,2,2,3]
val = 3
for i in range(len(nums)):

    while val 
    




# def BinarySearch(numbers = [2,7,11,15], target = 2):

#     left=0
#     right=len(numbers)-1
    
#     #note that these values are changing.
#     while left <= right:
#         mid = (left + right) // 2
#         if target < numbers[mid]:   
#             right = mid-1
#         elif target > numbers[mid]:
#             left = mid+1
#         else:
#             return mid


# print(BinarySearch())

    
        
        
# def twoSum(numbers,target):
#     ht={}
#     for i in range(len(numbers)):
#         if target-numbers[i] in ht:
#             return [ht[target-numbers[i]]+1,i+1]
            
#         ht[numbers[i]] = i
    
    # print(ht)
    
# print(twoSum([2,7,11,15],13))                    
# twoSum([2,7,11,15],13)