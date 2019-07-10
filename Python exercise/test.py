# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:03:45 2019

@author: brlam
"""



class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode=None

    


class LinkedList:
    def __init__(self):
        self.head = None
    
    #add to the beginning
    def addNode(self,data):
        #first, create a new node when this method is called.
        newNode=Node(data)
        #next, create a pointer and then point it to the head node; since newNode is created with Node constructor, it derives all its attributes to newNode (data and nextNode)
        newNode.nextNode=self.head
        self.head=newNode
    
    
#    def Print(self):
#        
#        if self.head==None:
#            self.head=self.head.nextNode
#        else:
#            print(self.head.data)
#            self.Print()
            
        
    def Print(self):
        while self.head!=None:
            print(self.head.data)
            self.head=self.head.nextNode
            
        
myList = LinkedList()
myList.addNode(1)
myList.addNode(2)
myList.addNode(3)
myList.addNode(4)
myList.Print()
