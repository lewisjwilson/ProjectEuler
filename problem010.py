# Question
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


# Solution - slow but functional

def isPrime(n):
    #numbers from 2 to square-root of N
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

primes = []
for x in range(2, 2000001):
    if isPrime(x):
        primes.append(x)
        
print(sum(primes))
