# Question
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


#Answer

def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

[largest, num1, num2] = [0, 0, 0]
for x in range(100, 1000):
    for y in range(100, 1000):
        product = x * y
        if product > largest and isPalindrome(product):
            largest = product
            num1 = x
            num2 = y

print("Largest =", largest, "\nx = ", num1, "\ny = ", num2)
