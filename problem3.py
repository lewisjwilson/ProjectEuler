# Question
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


# Answer

input = 600851475143
prime_factors = []
d = 2
while input > 1:
    while input % d == 0:
        prime_factors.append(d)
        input /= d
    d = d + 1

print(max(prime_factors))
