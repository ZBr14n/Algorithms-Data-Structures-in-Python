# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:25:09 2019

@author: Brian
"""

string=["aaa","ccbbb","aaaaaccccccc"]
s1="ccbbbaaaaacccccccaaa"
first=0
last=0

count=0


#check if its a different length
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        count=0
        i=len(a)-1
        j=len(b)-1
        carry=False
        newStr=""
        while i >= 0 or j >= 0:
            
            if a[i]!=b[j]:
                newStr="".join("1")
            else:
                #if both are equal to 1, carry 1 and join 0:
                if (a[i] and b[j])=="1":
                    carry=True
                    newStr="".join(["0",newStr])
                
                #if both are equal to 0, join 0:

                    
                    if carry==False
                    
#            if carry==True and (a[i] and b[j])=="1":
#                newStr="".join(["1",newStr])
#                    
                
                
                
                
            i-=1
            j-=1
        
        
        print(newStr)
        
        
obj=Solution()
obj.addBinary("11","1")
#print(obj.addBinary("11","1"))   #100
#print(obj.addBinary("1010","1011"))   #10101









"""
#            else:
#                carry=True
#                if carry and (a[i]=="1" and b[j]=="1"):
#                    newStr=newStr.join([a,b])
#                if carry and (a[i]!=b[j]):
#                    newStr=newStr.join([a,b])
            else:
                if (a[i] and b[j])=="0":
                    newStr="".join(["0",newStr])
                    
                if (a[i] and b[j])=="1":
                    newStr="".join(["1",newStr])
"""

