# Question

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.


# Solution

from itertools import permutations 
  
perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

valid = list()

for p in perm:
    [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10] = [str(p[0]), str(p[1]), str(p[2]), str(p[3]), str(p[4]), str(p[5]), str(p[6]), str(p[7]), str(p[8]), str(p[9])]
    
    if((int(d2+d3+d4)%2==0) and (int(d3+d4+d5)%3==0) and (int(d4+d5+d6)%5==0) and (int(d5+d6+d7)%7==0) and (int(d6+d7+d8)%11==0) and (int(d7+d8+d9)%13==0) and (int(d8+d9+d10)%17==0)):
        n = int(d1+d2+d3+d4+d5+d6+d7+d8+d9+d10)
        valid.append(n)
        print(f"{n} is such a pandigital number!")

print(f"Sum of valid pandigitals is {sum(valid)}.")
