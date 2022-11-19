# Question

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), 
# a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. 
# It is not possible to try every route to solve this problem, as there are 299 altogether! 
# If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all. 
# There is an efficient algorithm to solve it. ;o)


# Solution - same as solution for problem 18 (still valid!)

tri =[[59], # row 1
      [...],
      ...
      [...],
      [ ...,  63, 35]] # row 100

       
tri = tri[::-1]
rows = len(tri)

scores = []
scores = tri[0]
path = []

for row in range(rows):
    if row == 0:
        continue
    scores_temp = []
    cols = len(tri[row])
    for col in range(cols):
        cur_idx_score = tri[row][col] + scores[col]
        next_idx_score = tri[row][col] + scores[col+1]
        if(cur_idx_score > next_idx_score):
            scores_temp.append(cur_idx_score)
        else:
            scores_temp.append(next_idx_score)
    
    scores = scores_temp
    
print("score:", scores[0])
