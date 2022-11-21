# Question

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


# Solution (using the algorithm for next lexographic permutation on Wikipedia)
# (https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order)

import math

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(digits)
permutations = math.factorial(n)
print("Digits:", digits, "\nNumber of permutations:", permutations)

perms_count = 1

last_perm = sorted(digits)[::-1]

while True:
    
    for i in range(n-1):
        if digits[i] < digits[i+1]:
            ak = digits[i]
            k = i
       
    for i in range(k, n):
        if ak < digits[i]:
            l = i
            continue
    
    al = digits[l]
    
    digits[k] = al
    digits[l] = ak
    
    sub = digits[k+1::]
    rev = sub[::-1]
    digits = digits[:k+1] + rev
    
    perms_count += 1
    if(perms_count == 1000000):
        print(digits)
        print("1000000th permutation found!")
        break
