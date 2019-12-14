"""
hello
holle

brian
brain

leetcode
leotceed

aaacceee
bbbaeccc

1. If firstPtr is not vowel and lastPtr is vowel, keep moving firstPtr.
2. Vice versa for if firstptr is a vowel.
"""

def reverseVowels(s):
    i=0
    j=len(s)-1
    vowels="aeiouAEIOU"

    while i < j:
        
        if s[i] not in vowels:
            i+=1
        if s[j] not in vowels:
            j-=1
        
        
        
            
        