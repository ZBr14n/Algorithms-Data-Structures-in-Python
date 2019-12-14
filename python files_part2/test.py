#"{[]}"

def isValid(s="()"):

    stack=[]
    n=0
    for i in range(len(s)):
        stack.append(s[i])
        if s[i]=="]" or s[i]==")" or s[i]=="}": 
            n+=1
            if s[i-n]==stack[i]:
                print("works")           
                
                
    #scan string
    #for every left parenth, there needs to be right parenth eventually
    # the first right parenth MUST match with the first left parenth   

    #append left parenth on stack; once theres a right parenth, [n-1],[n-2] to determine if it matches  

#print(isValid())
isValid()