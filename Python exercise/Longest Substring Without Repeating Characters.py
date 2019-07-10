# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:35:45 2019
    for i,j in enumerate(s):
        if s[i] not in store:
            store.remove(s[i])
        
            
@author: brlam
"abcabcbb"

this is how it works:
pwwkew
 wwkew
  wkew
   kew
"""
##arr=[-2, -3, 4, -1, -2, 1, 5, -3]
##arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
def maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]):
     """
     :type nums: List[int]
     :rtype: int
     """
     for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
     return max(nums)
    
    
    
print(maxSubArray())


#def lengthOfLongestsubing(s="abcabcbb"):
#    sub=""
#    for i in range(len(s)):
#        j=i
#        #keep moving the pointer until duplicate char in sub
#        if s[j] not in sub:
#            sub+=s[j]
#            
#        
#            
#                
#    print(sub)
#
#
#
#
#
#lengthOfLongestsubing()


#def lastWord(s="Hello World test whitespace string otherwise"):
#    k=0
#    sub=0
#    a=0
#    for i in range(len(s)):
#        k+=1
#        if " "==s[i]:
#            i+=1
#            sub=len(s)-i
#    
#    
#    print(sub)
#                
#    
#lastWord()



#for i in S:
#    if i not in q:
#        q.append(i)
#    
#
#print(q)




#
#
#def lengthOfLongestsubing(s):
#      #012345
#    s="pwwkew"
#    #s="abcabcbb"
#    
#    s2=""
#    for i in s:
#        if i not in s2:
#            #s2=s2.join(i)
#            s2=s2.join(i)s
#    
#        print(s2,end='')
#
#    
#lengthOfLongestsubing("")
#
#    





#
#
#def solution(S):
#    occurrences = [0] * 26
#    
#    for i in range(len(S)):
#        occurrences[ord(S[i]) - ord('a')] += 1
#    
#    best_char = 'a'
#    best_res = 0
#    #the loop has to start at 1 because we need to use index 0 
#    for i in range(1, 26):
#    #if the count is greater than 0, do this below:
#        if occurrences[i] > best_res:
#            best_char = chr(ord('a') + i)
#            best_res = occurrences[i]
#    
#    return best_char
#    #return best_res
#
#
#
#print(solution(S="heello"))
#










    