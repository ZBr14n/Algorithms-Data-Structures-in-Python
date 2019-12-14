"""
Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]

1. For each elem in the array, check and extract the elems that are the same.
2. Store these into another array. 
3. Delete or set the value to NULL for elems that have been used already.
4. Keep doing this if value is not NULL. 
5. If there is no longer any matches, return false; else, return True.
"""

def hasGroupsSizeX(deck=[1,1,2,2,2,2]):
    