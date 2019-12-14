"""
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

# two pointer:
1. create two pointers; one for the first index, and the other for the last index.
2. create loop and traverse thru the array until the pointers meet and then stop.
3. Do this while the first element is swapped with the last element until they meet
at the middle index or the last indices have been swapped.

====================
# slow solution:
1. Loop the array from the back, and pop each one out and then assign it to variable.
2. Append this variable back to the array (this will push every elem once space to the right)

emadam
["b","r","i","a","n"]
["m","a","d","a","m","e"]

"""
# two pointer solution
def reverseString2(s=[]):
    i=0
    j=len(s)-1
    while len(s) > 1:
        #store element first before overriding it with last element.
        keep = s[i]
        s[i] = s[j]       
        s[j] = keep
        
        if i != j:
            i+=1
            j-=1
            if i > j:  #in case if the length of the string is even; since we are incr/decr i and j, we need to account the fact they will eventually cross each other so we break out of the loop.
                break
        else:
            break

    
    # return s
    print(s)

# slow solution
def reverseString(s=["m","a","d","a","m","e"]):
    ct = len(s)-1
    for i in range(len(s)-1,-1,-1):
        keep = s[i]
        
        if i > -1:
            s.append(keep)
    
    # scan the array again, pop each element out until the count is equal to length of the original string
    for j in range(len(s)):
        if j <= ct:
            s.pop(0)
    
    # print(s)
    return s

reverseString2()
# print(reverseString())