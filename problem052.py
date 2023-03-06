from itertools import permutations

def isPerm(n1, n2):
    n1_str = str(n1)
    n2_str = str(n2)
    
    n1_list = []
    n2_tuple= ()
    
    for d in n1_str:
        n1_list.append(int(d))
        
    n2_tuple = tuple(map(int, [*n2_str]))
    
    perm = permutations(n1_list)
    
    for p in perm:
        if(p==n2_tuple):
            return True
    
    return False


for i in range(1, 1000000):
    if(isPerm(i, 2*i) and isPerm(i, 3*i) and isPerm(i, 5*i) and isPerm(i, 5*i) and isPerm(i, 6*i)):
        print(i, 2*i, 3*i, 4*i, 5*i, "and", 6*i, "are all permutations of one another!")
        break
