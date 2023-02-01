def is_ra_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a) and a**2 + b**2 == c**2

p = 120

solutions = set()

for a in range(1, 100):
    for b in range(1,100):
        for c in range(1,100):
            if(is_ra_triangle(a, b, c) and a + b + c == p ):
                solutions.add((a, b, c))
                
solutions = set(tuple(sorted(l)) for l in solutions)

print(solutions)
