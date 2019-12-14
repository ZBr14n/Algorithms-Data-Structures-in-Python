"""
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

*note: if character does not repeat, we dont include an extra array for the count
1. create a new array to store.
2. Scan the input array with loop.
3. if the length of input is 1, we don't need to add an extra elem in the count.
4. Problem: how do we split the count if it is "12" in the array ["1","2"]?? convert the count to str.
5. As we loop, until there's new character, we have to count all same character(s) first before appending to new array
"""
#  aabbbc
#  abbbc
def compress(chars):
    store=[]
    count=1
    for i in range(len(chars)-1):
        # if there is repeat in arr
        if chars[i]==chars[i+1]:
            store.append(chars[i])
            count+=1
        else:
            # if [i] and [i+1] is no longer equal, then we add the count to the new array
            ct = str(count)
            for x in ct:
                store.append(x)
                
            store.append(chars[i])

    print(store)

# x=12
# print(type(x))
# x = str(x)
# print(type(x))
# for char in x:
#     print(char, end=' ')

compress(["a","b","b","b","b","b"])