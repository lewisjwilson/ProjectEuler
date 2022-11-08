# Question
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.


# Solution - Not very time efficient. Limits maybe could be calculated better.
# math.factorial() faster own factorial function, so replaced.

import math

def fsum(n):
    nstr = str(n)
    factsum = 0
    for d in nstr:
        fact = math.factorial(int(d))
        factsum += fact
    
    return factsum
 
sum = 0 
for i in range(3, 9999999+1):
    if(i == fsum(i)):
        sum += i
        print(i)
        
print("End of results.\nSum:", sum)
 
# Testing
# Finding the maximum n we need to check for
# Highest factorial we have is 9! (362880)
# Let's find the point where fsum(n) > n
# n = 9
# while True:
#     if(fsum(n) < n):
#         print("Max:", n)
#         break
#     else:
#         n = int(str(n) + '9')
#         continue
# Our upper bound is 9999999
