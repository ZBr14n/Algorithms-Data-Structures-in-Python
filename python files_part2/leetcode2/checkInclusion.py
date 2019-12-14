"""
Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

edge case:
abc bac bca 

--Make sure that the indices are in consecuritive order where the string elems form a substring
@return true if s2 contains the permutation of s1

1. Scan s1; retrieve the indices in s2 if each char in s1 matches in s2.
2. 
"""

