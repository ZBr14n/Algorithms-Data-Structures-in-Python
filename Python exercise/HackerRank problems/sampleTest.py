# -*- coding: utf-8 -*-
"""
Spyder Editor

write code to let * be the wildcard and match with any char.
"""


def isMember(words, query):
    #stores all characters 
    A = []
    for i in range(0,len(query)):
        if query[i]=="*":
            pass
        else:
            A.append(query[i])
    
    #grab the length of each string in the array.
    store = []
    for j in words:
        store.append(len(j))
    
      
      
    for x in store:
        if len(query) == x:
            if 
    
    

                
isMember(["foo", "bar", "baz"], "f*o")
        
        
#                return True
#            else:
#                return False
    
    
    
#isMember(["foo", "bar", "baz"], "f*o")

#print(isMember(["foo", "bar", "baz"], "f*o"))
        


#Explain the DS and algo? What is the runtime, space complexity and tradeoffs of the different approaches you talk about