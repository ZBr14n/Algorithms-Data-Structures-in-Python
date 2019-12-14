"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

-as we move slowPtr, we also incr. count by 1 also until 
count lands on fastPtr
-compare [i] and [i+1] to check for 1s

"""

def findMaxConsecutiveOnes(input):
    
    zero=0
    Res=0
    ct=1
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            ct+=1
        else:
            zero=0
            ct=1
            
        Sum = max(ct,zero)
        
    
    return Sum
        
print(findMaxConsecutiveOnes([1,1,1,1,0,1,1,1]))
# findMaxConsecutiveOnes([1,1,0,1,1,1])
# print(findMaxConsecutiveOnes([1,1,0,1,1,1]))        