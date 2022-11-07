# Question
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# Solution
# Generate all permutations of 1..9
# Operate only on 2x3 or 1x4 numbers as per prior testing for optimisation.

from itertools import permutations

# testing limits and max/min combinations
# print("Need to utilise 9 number spaces.")
# print("\nMin 2x2 nums (12x34):", 12*34)
# print("Max 2x2 nums (98x76):", 98*76)
# print("Min: 7, Max 8 - 2x2 Not Applicable.")
# print("\nMin 2x3 nums (12x345):", 12*345)
# print("Max 2x3 nums (98x765):", 98*765)
# print("Min: 9, Max 10 - 2x3 Somewhat Applicable.")
# print("\nMin 3x3 nums (125x234):", 125*234)
# print("Min: 11 - 3x3 Not Applicable.")
# print("\nMin 1x4 nums (1x2345):", 1*2345)
# print("Max 1x4 nums (9x8765):", 9*8765)
# print("Min: 9, Max = 10 - 1x4 Somewhat Applicable.")

# patterns must either be of the form 2x3 or 3x2

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
perms = list(permutations(nums))
results = set()

for perm in perms:
    two = int(perm[0] + perm[1])
    three = int(perm[2] + perm[3] + perm[4])
    res = int(perm[5] + perm[6] + perm[7] + perm[8])
    if two * three == res:
        results.add(res)
        print(two, "x", three, "=", res)
    
    one = int(perm[0])
    four = int(perm[1] + perm[2] + perm[3] + perm[4])  
    res = int(perm[5] + perm[6] + perm[7] + perm[8])
    if (one * four == res):
        results.add(res)
        print(one, "x", four, "=", res)
    
print("Sum of products:", sum(results))
