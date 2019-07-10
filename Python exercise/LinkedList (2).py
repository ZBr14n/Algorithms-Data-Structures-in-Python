# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:16:55 2019

    for i in range(0,26):
        r = random.randint(97,122)
        print(chr(r),end=' ')

@author: brlam
Write a reverse Hangman game in which the user thinks of a 
word and the computer tries to guess the letters in that
word. The user tells the computer how many letters the word contains.
"""
import random

def ComputerGuess(userInput):
    
    #coount correct guesses
    correct=0
    #count incorrect guesses
    wrong=0
    #
    storeWrongChars={}
    
#    for i, letters in enumerate(userInput):
#        remainingLetters[i] = letters
        
    guess=0
    myInput="f"
    while myInput=="f":
        r = random.randint(97,122)
        print("Is it:  " + chr(r))
        myInput = input()
        if myInput=="f":
            storeWrongChars[myInput,guess]=0
            guess+=1
            
    print(storeWrongChars)


ComputerGuess("brian")