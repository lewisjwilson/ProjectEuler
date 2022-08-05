# Question
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?


# Solution

# How to calculate lattice paths:
# https://en.wikipedia.org/wiki/Lattice_path#Combinations_and_NE_lattice_paths

n = 20
k = 20
import math
print("From (0,0) to (20,20), there are",math.comb(n+k, n),"path combinations.")
