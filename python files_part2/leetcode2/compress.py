"""
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

1. If [i] and [i+1] are diff, copy [i] and the count to be inserted into new array. 

"""
def compress(input):
    ct=1
    arr=[]
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            ct+=1
            if i+1==len(input)-1:
                arr.append(input[i+1])
                arr.append(ct)
        else:
            arr.append(input[i])
            arr.append(ct)
            ct=1


    
    arr = ''.join(str(e) for e in arr)
    print(arr)        


compress(["a","a","b","b","c","c","c"])
compress(["a","a","a"])
compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])

# def compress(input):
#     aux = []
#     ct = 1
#     for i in range(len(input)-1):
        
#         if input[i] == input[i+1]:
#             ct+=1
            
#         else:
#             aux.append(input[i])
#             aux.append(ct)
#             ct = 1
        
#     print(aux)        
    

            
            
            
            
        