# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 23:06:07 2019

@author: Brian
"""

import random

store={}
count=0
for i in range(0,5):
    r = random.randint(97,122)

    if chr(r) not in store:
        store.setdefault(chr(r),"")
    else:
        count+=1        
        store[chr(r)]=count


print(store)


