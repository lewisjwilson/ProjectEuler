# Question
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?


# Solution - finding prime factors to enable efficient computation.
# e.g. 6^24 = ((((6^2)^2)^2)^3)...RHS more efficient than LHS
# [Prime Factors of 24 are 2, 2, 2 and 3] - store these as a list and iterate
# This code works for any base and exponent


import math

def primeFactors(n):
    prime_factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            prime_factors.append(d)
            n /= d
        d = d + 1
    return prime_factors

def calcExp(base, prime_factors):
    ans = base
    for x in pf:
        ans = ans ** x
    return ans

exponent = 1000
base = 2
pf = primeFactors(exponent)
ans = calcExp(base, pf)

sum_list = [int(x) for x in str(ans)]
print(sum(sum_list))
