"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle 
is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

aabbaaa, bba   output 2

KMP string search:
1. Loop thru needle; check if [i] and [i+1], 


####
1. Scan the needle, and check if each letter is in the haystack.
2. Not only do the letters should be in the haystack, the indices must be in consequent order, 
(e.g.  elements should be i+1 apart from each other, like index 2,3,4)


"""
# check if needle follows consequent order when we compare it back and forth with the haystack.
def strStr(haystack,needle):


# strStr("hello","ll")            
strStr("aabbaaa","bba")