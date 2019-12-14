"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
"""

"""
1. Outer loop goes thru the lists itself from index 0 to index 2.
2. Inner loop goes thru the individual letters of the string for each index in the list.
3. We scan the whole string for index 0; for other indexes we only need to scan until the prefix
match and then we can move on until the lists ends.
4.

# the letters in index 1 should be match elem in index 0;
# index 2 should match index 1 and return the prefix
"""
# returns a string for the prefix
# ["dog","racecar","car"]
# ["flower","flow","flight"]
# ["flower","flight","flow"]
# ["dog","racecar","car"]
def longestCommonPrefix(strs=["dog","racecar","car"]):
    tmp=""
    if len(strs)==1:
        return strs[0]
    else:
        for index in strs[1:]:
            tmp=""
            for i in range(len(index)):
                if index[i] in strs[i-1]:
                    tmp+=index[i]
                else:
                    break
        
    return tmp

# longestCommonPrefix()
print(longestCommonPrefix())