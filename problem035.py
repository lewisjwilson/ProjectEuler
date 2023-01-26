def cyclic_values(n):
    number = str(n)
    cyclic = []
    for i in range(len(number)):
        number = number[1:] + number[0]
        cyclic.append(number)
    
    return cyclic

def isPrime(n):
    #numbers from 2 to square-root of N
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

count = 0

for i in range(2, 1000000):
    cyclic_nums = cyclic_values(i)
    all_prime = True
    for num in cyclic_nums:
        if(not isPrime(int(num))):
            all_prime = False
            break
    if(all_prime):
        print(i)
        count += 1
        
print(count)
