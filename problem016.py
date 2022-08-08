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


exponent = 24
base = 6

pf = primeFactors(exponent)
print(pf)

ans = 1
for x in pf:
    ans *= base ** x
    print(ans)

print(ans)
