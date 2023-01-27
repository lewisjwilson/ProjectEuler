# Question

# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# Solution

def trunc_values(n):
    number = str(n)
    temp = number
    trunc = []
    trunc.append(number)
    for i in range(len(number)-1):
        number = number[1:]
        trunc.append(number)
    
    for i in range(len(temp)-1):
        temp = temp[0:len(temp)-1]
        trunc.append(temp)
        
    return trunc

def isPrime(n):
    if(n<2):
        return False
    #numbers from 2 to square-root of N
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

count = 0
# Excluding values below 10 as non-truncatable
i = 10
trunc_primes = list()

while(count<11):
    trunc_nums = trunc_values(i)
    all_prime = True
    for num in trunc_nums:
        if(not isPrime(int(num))):
            all_prime = False
            break
    if(all_prime):
        print(i)
        trunc_primes.append(i)
        count += 1
    
    i += 1
        
print(f"The 11 truncatable primes are {trunc_primes}.\nThey have a sum of {sum(trunc_primes)}!")
