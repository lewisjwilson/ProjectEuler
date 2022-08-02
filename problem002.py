# Question
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


# Answer

# starting at n = 3
fib_2 = 1  # current - 2 term
fib_1 = 2 #current - 1 term
fib = 3 # current term
sum = 2

while fib <= 4000000:
    if fib % 2 == 0:
        sum = sum + fib
    fib_2 = fib_1
    fib_1 = fib
    fib = fib_2 + fib_1
print(sum)