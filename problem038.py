
def is_pandigital(n):
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    compare = [int(x) for x in str(n)]
    return (digits == sorted(compare))
    

pandigitals = []

for test in range(1,1001):
    saved = []
    for n in range(1, 10):
        saved.append(test*n)
        s = ''.join([str(i) for i in saved])
        if(len(s)==9 and is_pandigital(int(s))):
            pandigitals.append(s)
            print(s)
        

print(pandigitals)
