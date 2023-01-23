# Question 
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


# Solution

# This solution works using math that converts fractions into decimals.
# First, you find the integer and remainder part (integer: floor(num/den), remainder: (num % den)/den)
# Then at each step:
# 1. Multiply remainder by 10
# 2. Append the remainder/den to the current result
# 3. Find new remainder = remainder % den

import math

def recurring_part(num, den):
    output = ""
    
    # A map to check for already seen values
    seen = {}
    
    # First remainder
    rem = num % den
    
    while (rem != 0) and (rem not in seen):
        # Store the remainder
        seen[rem] = len(output)
        
        # Multiply the remainder by 10
        rem *= 10
        
        # Append the remainder/denominator to the output
        output += str(rem//den)
        
        # Update the remainder
        rem = rem % den
        
    if(rem == 0):
        return "0"
    else:
        return output[seen[rem]:]

d = 0
largest = 0
cycle = ""

for i in range(1, 1001):
    r = recurring_part(1, i)
    if(r != "0"):
        if(len(r) > largest):
            d = i
            cycle = r
            largest = len(r)
print(f"1/{d} has the largest recurring cycle.\nIt has {largest} digits.\nThose digits are:\n{cycle}")
