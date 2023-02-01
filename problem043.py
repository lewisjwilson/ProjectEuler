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

def check(d):
    if((int(d[0]+d[1]+d[2])%2!=0) or \
       (int(d[2]+d[3]+d[4])%3!=0) or \
       (int(d[3]+d[4]+d[5])%5!=0) or \
       (int(d[4]+d[5]+d[6])%7!=0) or \
       (int(d[5]+d[6]+d[7])%11!=0) or \
       (int(d[6]+d[7]+d[8])%13!=0) or \
       (int(d[7]+d[8]+d[9])%17!=0)):
        return False
    return True
    
perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

valid = list()

for p in perm:
    
    d = list(p)
    d = [str(x) for x in d]
    
    if(check(d)):
        n = int(d[0]+d[1]+d[2]+d[3]+d[4]+d[5]+d[6]+d[7]+d[8]+d[9])
        valid.append(n)
        print(f"{n} is such a pandigital number!")

print(f"Sum of valid pandigitals is {sum(valid)}.")
