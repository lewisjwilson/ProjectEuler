# Question
#
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


# Solution

number = list()

# Generate array of integers
for i in range(1000000):
    number.append(i)

# Convert int array to string array and split to string
d = ''.join([str(x) for x in number])

# For values 1, 10, ..., 1000000, get the index of the integer
output = 1
for x in (10**p for p in range(7)):
    output *= int(d[x])

print(f"Output of (d_1 * ... * d_1000000) is {output}")
