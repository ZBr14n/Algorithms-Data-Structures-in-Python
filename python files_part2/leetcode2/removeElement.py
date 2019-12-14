"""
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Given nums = [3,2,2,3], val = 3,

1. Use for loop and set it to first element; declare a count variable before the while loop
which keeps incrementing until end of array.
2. while val is not equal to nums[i], incr. ct. 
"""

def removeElement(nums,val):
    ct=0
    for el in nums:
        
        i=0
        while i <= len(nums)-1:
            if nums[i] != val:
                ct+=1
            i+=1

        return ct

    


# removeElement([0,1,2,2,3,0,4,2],2)
# print(removeElement([0,1,2,2,3,0,4,2],2))
print(removeElement([3,2,2,3],3))
# print(removeElement([0,1,2,2,3,0,4,2],3))