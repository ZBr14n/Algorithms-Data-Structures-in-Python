# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:55:04 2019

@author: Brian
https://app.codility.com/programmers/lessons/90-tasks_from_indeed_prime_2015_challenge/longest_password/
The goal is to choose the longest word that is a valid password. 

"""
#a-z    , A-Z  ,    0-9     
#97-122 , 65-90,    48-57
#

#even # of letters
#odd # of digits


def oddDigits(s="pass007"):
    k=0
    for i in s:
        if i.isdigit():
            k+=1
    
    if k%2!=0:
        return(True)
    
    return(False)
    
    
def evenLetters(s="pass007"):
    k=0
    for i in s:
        if i.isalpha():
            k+=1
    
    if k%2==0:
        return True

    return(False)


def isAlphaNum(s="?xy1"):
    for i in s:
        if not i.isalnum():
            print(i)


def countWords(s="test 5 a0A pass007 ?xy1"):
    k=1
    for i in s:
        if i==" ":
            k+=1
    print(k)


countWords()


#  4 =  0100
#  1 =  0001 
# if you 'and' the digits, this above will be 0 hence 4 is even


#  5 =  0101
#  1 =  0001 
# if you 'and' the digits, this above will be 1 hence 5 is odd.

