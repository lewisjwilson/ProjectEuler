original = [
  [4445,2697, ...]
            , ... , 
            [ ... ]
           ]
          
size = len(original)

updated = list()
for i in range(size):
    updated.append([0]*size)

def pupd():
    for x in updated:
        print(x)
    print()

def pori():
    for x in original:
        print(x)
    print()
    
#pori()

updated[0][0] = original[0][0]

# 1st Pass
for y in range(size):
    updated[y][0] = updated[y-1][0] + original[y][0]

for x in range(size):
    updated[0][x] = updated[0][x-1] + original[0][x]
    x+=1

# 2nd Pass+
for x in range(1, size):
    for y in range(1, size):
        if(updated[y-1][x]<updated[y][x-1]):
            updated[y][x] = original[y][x] + updated[y-1][x]
        else:
            updated[y][x] = original[y][x] + updated[y][x-1]

#pupd()

print(f"The minimal path is {updated[size-1][size-1]}.")
