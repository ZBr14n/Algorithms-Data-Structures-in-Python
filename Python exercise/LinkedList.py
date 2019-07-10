# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:03:45 2019

@author: brlam
"""

#implement linked lsit
class Node:
    def __init__(self,data):
        self.value = data
        self.nextNode=None
        
    def Print(self):
        print("|" + str(self.value) + "|->",end=' ')
        if self.nextNode != None:
            self.nextNode.Print()
        
    
class LinkedList:
    def __init__(self):
        self.head = None
        

    def addNode(self,data):
        newNode = Node(self.head,data)
        self.head = newNode
    
    
    def printNodes(self):
        pass



myNodes=Node(1)
myNodes.nextNode=Node(2)
myNodes.nextNode.nextNode=Node(3)
myNodes.Print()
