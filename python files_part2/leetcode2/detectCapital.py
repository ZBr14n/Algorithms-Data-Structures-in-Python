
def solution(s):
    
    #FlaG

    for i, char in enumerate(s):
        flag = True
        if (65 <= ord(s[0]) <= 97) and i >= 1 and (97 <= ord(s[i]) <= 123):
            flag=True
        else:
            flag=False
        
    print(flag)

# print(solution("Flag"))        
solution("FlaG")