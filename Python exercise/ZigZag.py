


def isPrime(val=17):
    
    for i in range(2,val):        
        if val%i==0:
            return False
    else:
        return True

        
#isPrime()
print(isPrime())