# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 21:49:30 2019

@author: Brian
Input: n = 10, pick = 6
Output: 6
"""
#
#import random
#
#arr=[n for n in range(1,11)]
#pick=random.randint(1,10)
#
#while True:
#    #divide sorted array in half
#    #continue doing it  until the Pick is found
#    #user guesses, then computer responds whether it is too high or not.
#    
#    #every time when a user guesses wrong, we divide the arr in half, and only want the half that the Pick is in.
#    print("guess here: ")
#    u=int(input())
#    if u > pick:
#        #if pick is 3, but user guess 6
#        arr=arr[len(arr)//2]
#    
#    
#    break
#
#
#print(arr)
#    
#    
#    






















    
#arr=[n for n in range(1,11)]
#pick=6
#mid=len(arr)//2
#
#while True:
#    u = int(input())
#    
#
#    if u < pick:
#        del arr[:mid]
#        print("My number is Higher")
#    if u > pick:
#        del arr[mid:]
#        print("My number is Lower")
#        
#    
#    if u==pick:
#        print("Congrats! You got it!")
#        break
#    
#    
#    print(arr)

    
 
    
    
    









#
#def guessNumber(n=10):
#    
#    #loop user input 
#    #compare 6 with each user input.
#    #if pick is not 6 
#    
#    rand = random.randint(1,10)
#    while True:
#        print("guess here: ")
#        user=int(input())
#        if user>rand:
#            print("My number is lower")
#        if user<rand:
#            print("My number is Higher")
#
#
#        if user==rand:
#            print("Congrats! You got it!")
#            break
#
#
#
#guessNumber()


#
#def solution(A):
#    a=min(A)
#    b=max(A)
#    #for i in range(len(A)):
#    
#
#    #compare lowest num with the first ele in array
#    #if a+1 is equal to first ele, incr count++
#    #account for nums before a+1 and after a+1
#    #check that it comes before the lowest num and make sure its number that is just 1 away from each other.
#    count=0
#    sum=0
#    tmp=0
#    for i in A:
#        if i!=a and A.index(i) < A.index(a):
#            tmp=i
#            continue
#        else:
#            count+=1
#        
#        if tmp+1==i:
#            count+=1
#        
#        
#        
#                
#        #before the lowest
##        if A.index(i) < A.index(a) and a+1==i:
##            sum=i+1
##            count+=1
##        if sum==i:
##            count+=1
#
#            
#        #after the lowest
##        if A.index(i) > A.index(a) and i==a+1:
##            count+=1
#        
#        
#        
#        #if 5 is last index, incr count
#        if A.index(b)==len(A)-1:
#            count+=1
#        
#            
#    print(count)
#
#
#
#A=[2,1,3,5,4]
##A=[2,3,4,1,5]
##A=[1,3,4,2,5]
#solution(A)
#
#










#AM/PM is located at index 8 and 9
#def timeConversion(s="00:05:45AM"):
#    store=""
#    
#    tmp=s[0:2] #hour
#    tmp2=s[8:10] #AM/PM
#    
#    #convert to military time.
#    if s[0:2]=="12" and tmp2=="PM":
#        return s[0:8]
#    if s[0:2]!="12" and tmp2=="PM":
#        store=int(tmp)+12
#        s=s.replace(s[0:2],str(store))
#        return s[0:8]
#    
#
#    
#    if s[0:2]=="12" and tmp2=="AM":
#        s=s.replace(s[0:2],"00")
#        return s[0:8]
#    if s[0:2]!="12" and tmp2=="AM":
#        return s[0:8]
#    
#    return "None"
#    
#
##timeConversion()
#print(timeConversion())


#def birthdayCakeCandles(ar=[3,7,1,13,4,13,13]):
#    #find highest num in array
#    tmp=ar[0]
#    count=1
#    for i in range(len(ar)-1):        
#        if tmp < ar[i+1]:
#            tmp=ar[i+1]
#        if tmp in ar:
#            count+=1
#    
#    count=0
#    for i in ar:
#        if i==tmp:
#            count+=1
#    
#    print(count)
#
#
#
#birthdayCakeCandles() 
       
#
#def myPow(x,n):
#    origN=n
#    count=1
#    
#    if n < 0:
#        n=abs(n)
#    
#    temp=x
#    while True:
#        
#        temp*=x
#        #print(count)
#        
#        count+=1
#        if count==n:
#            break
#        
#    
#    if origN < 0:
#        temp=1/temp
#        
#    print(temp)
#    
#
#myPow(2,-15)

#myPow(2.00000,10)
#myPow(2.10000,3)
#myPow(2.00000,-2)

