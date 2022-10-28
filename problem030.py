# Question
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


# Solution
# We need a number n*pow(9, 5) that is n digits long.
# Since 9**5 = 59049, we need at least 5 digits for the max
# 5*pow(9, 5) = 295245 ( 5 digits ) ...possible
# 6*pow(9, 5) = 354294 ( 6 digits ) ...possible
# 7*pow(9, 5) = 413343 ( 6 digits ) ...cannot as n is 7 on the LHS and 6 on the RHS, it cannot satisfy our requirements, so we take 6*pow(9, 5) to be the maximum. 

max = 6*pow(9, 5)
print("Max:", max)
sum = 0
for i in range(10, max):
    s = str(i)
    temp = 0
    for digit in s:
        temp += pow(int(digit), 5)
    
    if(temp == i):
        sum += temp
        print(i, temp)
    
print(sum)
