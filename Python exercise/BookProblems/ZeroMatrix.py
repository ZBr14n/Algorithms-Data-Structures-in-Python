# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:14:31 2019

@author: Brian
Zero Matrix: Write an algorithm such that if an element in 
an MxN matrix is 0, its entire row and column are set to 0

-double for loop to generate rows and columns on lists.
-once position is placed, entire row and column cover by 0
"""

#def Matrix(x,y):
#    ROW = [1] * 5
#    COLUMN = [1] * 5
#    
#    for i in range(5):
#        print("1",end=' ')
#        for j in range(4):
#            print("1",end=' ')
#        
#        
#        print("\n")
        



import numpy 
  
# initializing matrices 
x = numpy.array([[1, 2], [4, 5]]) 
y = numpy.array([[7, 8], [9, 10]]) 
  
# using add() to add matrices 
print ("The element wise addition of matrix is : ") 
print (numpy.add(x,y)) 

#Matrix(1,1)