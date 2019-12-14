"""
Given an array of size n, find the majority element. The majority element is the
element that appears more than ⌊ n/2 ⌋ times.

1. Find the midpoint of an array; if the count is greater than the midpoint for an elem, we
know that this is the majority element.
2. Create another pointer j which starts at [i+1], if it equals, incr. the count.
3. If count is greater/equal to the midpoint then it is a majority Elem.

[3,2,3]
[2,2,1,1,1,2,2]
"""

def majorityElement(input):

    mid = round(len(input)/2)
    ct = 0
    for i in range(len(input)):
        j = i+1
        while ct < mid and j != len(input)-1:
            if input[i]==input[j]:
                ct+=1
                j+=1
            else:
                j+=1
                        
            j=0                   
    
    print(ct)





# print(majorityElement([3,2,3]))
# print(majorityElement([2,2,1,1,1,2,2]))
majorityElement([2,2,1,1,1,2,2])
majorityElement([3,2,3])