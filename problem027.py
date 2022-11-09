# Question
#
# Euler discovered the remarkable quadratic formula: n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. 

# However, when n = 40, the formula is divisible by 41, and certainly when n = 41, it is clearly divisible by 41.
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79.
# The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form: n^2 + an + b, where mod(a) < 1000 and mod(b) <= 1000
# where n is the modulus/absolute value of n. [e.g. mod(11) = 11 and mod(-4) = 4]

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes 
# for consecutive values of n, starting with n = 0.

# Solution

def isPrime(n):
    if(n<2):
        return False
    #numbers from 2 to square-root of N
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n = 1
primes = 0
primes_max = 0
a_max = 0
b_max = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        while(isPrime(n**2 + a*n + b)):
            #print(n**2 - a*n + b, "is prime")
            n += 1
            primes += 1
            
        if(primes>primes_max):
            primes_max = primes
            a_max = a
            b_max = b
            
        n = 0
        primes = 0
    
print("a =", a_max, ", b =", b_max, "("+str(primes_max)+" primes)")
print("a * b =", a_max*b_max)
