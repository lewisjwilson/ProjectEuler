def isPrime(n):
    #numbers from 2 to square-root of N
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
def rotate(n, l):
    nstr = str(n)
    if(l>1):
        return(nstr[l-1] + nstr[:l-1])
        

circular = set()
circular.add(2)
circular.add(3)
circular.add(5)
circular.add(7)

for i in range(2, 100001):
    test = i
    l = len(str(i))
    #print(l)
    if(not isPrime(int(test))):
        continue
    if(l==1):
        continue
    for j in range(1, l+1):
        test = rotate(test, l)
        if(isPrime(int(test))):
            #print("num:",test, "iter:", j)
            if(j == l):
                circular.add(i)
                #print(i, "SUCCESS")
        else:
            #print(i, "FAIL")
            break
        
print(circular)
