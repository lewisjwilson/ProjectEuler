import re

f = open("0059_cipher.txt", 'r')

lines = f.read().split(',')


# Testing
# for key1 in range(97, 123):
#     for key2 in range(97, 123):
#         for key3 in range(97, 123):

#            key = chr(key1)+chr(key2)+chr(key3)

#            out = list()
#            count = 0
#            first = True
#            second = False
#            third = False
#            for l in lines:

#                if(first):
#                    out.append(chr(int(l)^key1))
#                    first = False
#                    second = True
#                elif(second):
#                    out.append(chr(int(l)^key2))
#                    second = False
#                    third = True
#                elif(third):
#                    out.append(chr(int(l)^key3))
#                    third = False
#                    first = True

#                count += 1
                # For narrowing down and locating legible english manually
                #if(count==10):
                #    
                #    s = ''.join(out)
                #    if(all(chr.isalpha() or chr.isspace() for chr in s)):
                #        print(key)
                #        print(s)
                #    break
                
key = 'exp'
out = list()
ascii_sum = 0

first = True
second = False
third = False

for l in lines:
    if(first):
        c = chr(int(l)^ord(key[0]))
        out.append(c)
        first = False
        second = True
    elif(second):
        c = chr(int(l)^ord(key[1]))
        out.append(c)
        second = False
        third = True
    elif(third):
        c = chr(int(l)^ord(key[2]))
        out.append(c)
        third = False
        first = True
    
    ascii_sum += ord(c)

print(''.join(out))
print(ascii_sum)
