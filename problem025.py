# Question
# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# F1 = 1, F2 = 1, F3 = 2, F4 = 3, F5 = 5, F6 = 8, F7 = 13, F8 = 21, F9 = 34, F10 = 55, F11 = 89, F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# Solution - Generate temp fibonacci terms with an index counter (i). When i the term length reached 1000, print the index value
f_1 = 1
f_2 = 1
i = 3
while True:
    f = f_2 + f_1
    f_2 = f_1
    f_1 = f
    if len(str(f)) == 1000:
        break
    i+=1
    
print(i) 
