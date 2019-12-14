"""
"A man, a plan, a canal: Panama"

1. switch all letters to lowercase and take out the spaces, and punctuations.
2. reverse the strings and compare to original string, if they are equal then they are palindromes.
"""
# implement the two pointer solution here:


# regular string manip. solution
def isPalindrome(s):
    if s=="":
        return True
    else:    
        s = ''.join(s.split(' '))
        s = s.lower()
        
        store=[]
                
        for chars in s:
            if chars.isalnum():
                store.append(chars)

        store = ''.join(store)

        if store[::-1] == store:
            return True

    return False    
    
print(isPalindrome("racecar"))
# "race a car"
# "A man, a plan, a canal: Panama"