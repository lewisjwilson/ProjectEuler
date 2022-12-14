# Question 
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.


# Solution

def Collatz(value):
    if value % 2 == 0:
        return value/2
    else:
        return 3*value + 1

value = 0
count = 0
hi_value = 0
hi_count = 0
for x in range(13, 1000001):
    value = x
    while value != 1:
        count += 1
        value = Collatz(value)
    if count > hi_count:
        hi_count = count
        hi_value = x
    count = 0

print(hi_value,"produces the longest Collatz chain with", hi_count,"numbers in the sequence." )
