# Question
# The sum of the squares of the first ten natural numbers is,  1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# Solution

n = 100

# sum of natural numbers: n(n+1)/2
square_of_sum = ((n*(n+1))/2)**2

sum_of_squares = 0
for i in range(n+1):
    sum_of_squares += i**2

print(abs(int(square_of_sum - sum_of_squares)))
