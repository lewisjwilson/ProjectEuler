# Question
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Solution - get list of squares and iterate through the list. 
# if a^2 + b^2 = c^2 and a + b + c = 1000, print the answer of a*b*c

n = 1000 #10^2

squares = []
num = 1
while num**2 <= n**2:
    squares.append(num**2)
    num += 1

def findABC(list):
    for a_sq in squares:
        for b_sq in squares:
            for c_sq in squares:
                if a_sq + b_sq == c_sq and int(a_sq**0.5 + b_sq**0.5 + c_sq**0.5) == 1000:
                    print(a_sq, b_sq, c_sq)
                    return [a_sq, b_sq, c_sq]

        
abc = findABC(squares)
a = int(abc[0]**0.5)
b = int(abc[1]**0.5)
c = int(abc[2]**0.5)

print("a =", a,"b =", b,"c =", c,"\nSummation =",int(a+b+c), "\nProduct =",int(a*b*c))
