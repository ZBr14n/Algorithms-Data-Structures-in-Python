# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:58:30 2019

@author: brlam
"""


# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        