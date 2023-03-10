import math
from itertools import permutations

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True
    
seen = set()
flag = False

savedNum = "0"

for n in range(100, 1000):
    numStr = "***" + str(n)
    perms = [''.join(p) for p in permutations(numStr)]
    #print(perms)
    
    for s in perms:
        if s in seen:
            continue
        seen.add(s)
        count = 0
        for i in range(10):
            temp = s
            temp = temp.replace("*", str(i))
            num = int(temp)
            if(is_prime(num) and temp[0] != "0"):
                count+=1
                
        #print(s, "is a", count, "prime value family.")
        if(count==8):
            print(s, "is a", count, "prime value family!!!!!!!!!!!")
            savedNum = s
            flag = True
    if(flag):
        break

if savedNum == "0":
    print("No 8 prime value families found...")
else:
    for i in range(10):
        temp = savedNum
        temp = temp.replace("*", str(i))
        num = int(temp)
        if(is_prime(num)):
            print(temp, "is prime!")
