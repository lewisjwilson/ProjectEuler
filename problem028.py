# Question

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# *21  22  23  24 *25
#  20  *7  8   *9  10
#  19   6  *1   2  11
#  18  *5   4  *3  12
# *17  16  15  14 *13

# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


# Solution : Initially, it appears that a matrix needs to be created and worked on.
# However, after analysing carefully, you can see that from the centre working up and right,
# These values are square numbers of 1, 3, 5, 7, 9... (odds). 
# You can then work out the relationship between those numbers and their spiral sublevel numbers
# That is, top right: square, top left = square - odd_num, bottom_left = square - 2(odd_num), 
# bottom_right = square - 3(odd_num)
# Putting it together, we have all diagonal values when adding to a list. (Initialising with 1
# and iterating from 3, to 1001.

diags = [1]
for num in range(3, 1002, 2):
    sq = num*num
    minus = num-1
    diags.append(sq)
    diags.append(sq-minus)
    diags.append(sq-2*minus)
    diags.append(sq-3*minus)
 
print(sum(diags))
