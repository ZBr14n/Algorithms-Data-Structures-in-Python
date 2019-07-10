# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:35:26 2019

@author: Brian
"""
from collections import deque

q=deque(["test1","test2","test3"])
q2=deque(["test1","test2","test3","test4"])
q.extendleft(q2)
print(q)

#q.append("brian")
#print(q)
#q.appendleft("brian")
#print(q)
#q.popleft()
#print(q)





#stack.append("brian")
#print(stack)
#
#print(stack.pop())
#print(stack)