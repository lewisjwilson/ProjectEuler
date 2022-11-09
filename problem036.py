# Question
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)


# Solution

def isPalindrome(n):
    return str(n) == str(n)[::-1]
        
sum = 0
for i in range(1, 1000000):
    if(isPalindrome(i) and isPalindrome(bin(i)[2:])):
        sum += i
        print(i, "and", bin(i)[2:], "are palindromes.")
    
print(f"Sum of palindromes (base-10): {sum}")
