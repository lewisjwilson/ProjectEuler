# Question
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Solution - check each incrementing number for primeness, increment count of primes until reaching n.

n = 10001
current_num = 2

def isPrime(n):
    #numbers from 2 to square-root of N
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

count = 0
while count < n:
    if isPrime(current_num):
        count += 1
    if count != n:
        current_num += 1

print(n,"th prime number = ", current_num)
