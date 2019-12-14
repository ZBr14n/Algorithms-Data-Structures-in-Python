"""
count and find vowels:/find consonants:

1. list the vowels of the alphabet; anything that is NOT a vowel, must be a consonant.
2. Loop thru the string and keep count of which is a vowel or not (create method)
3. Store vowels as a key and the count as a value in a hash table.
4. Find the length of the string and subtract the sum count of vowels to get the number of 
consonants. 
"""

def solution(str):
    ht={
        'a':0,
        'e':0,
        'i':0,
        'o':0,
        'u':0,
        'y':0
    }    
    keep=""
    whitespace=0
    for i in range(len(str)):
        if str[i].isupper() or str[i] in ht:
            keep=str[i].lower()
            if keep in ht:
                ht[keep]=ht.get(keep)+1
        if str[i].isspace():
            whitespace+=1

    Sum=0
    for x in ht.values():
        Sum+=x

    
    print("# vowels: ", "{}".format(Sum))
    print("# consonants: ", "{}".format(len(str)-Sum-whitespace))


# solution("brIAn")                
# print(ht)
# solution("HellO")
# solution("I am happy")
solution("there is a quiet Mouse")