import math


def triNum(n):
    triangle_number = 0
    for i in range(1, n+1):
        triangle_number += i
    return triangle_number


def getDivisors(number):
    divisors = []
    for i in range(1, number+1):
        if(number % i == 0) and i not in divisors:
            divisors.append(i)
    return divisors


# which triangle number? (n = nth term in sequence)
n = 1
triangle_number = triNum(n)
divisors = getDivisors(triangle_number)
while len(divisors) < 500:
    n += 1
    triangle_number = triNum(n)
    divisors = getDivisors(triangle_number)

print(triangle_number, divisors)
