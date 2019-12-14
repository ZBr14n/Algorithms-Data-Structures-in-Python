"""
"1234"
1. Scan thru the string; for each char, get the ascii code of the char and subtract it by 0
to convert the string to integer.
"""

def convert(s):
    store=[]
    for i,j in enumerate(s):
        store.append(ord(j)-ord('0'))
        print(type(store[i]))
    print(store)
    print(type(store))

convert("1234")