# Question
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
# which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


# Solution

fracs = []

for num in range(10, 100):
    numstr = str(num)
    for den in range(10, 100):
        if(num>=den):
            continue
        
        denstr = str(den)
        
        for digit in numstr:
            if digit in denstr and digit != "0":
                whole_frac = int(numstr)/int(denstr)
                
                cancel_num = int(numstr.replace(digit, "", 1))
                cancel_den = int(denstr.replace(digit, "", 1))
                
                if cancel_den != 0:
                    cancel_frac = cancel_num/cancel_den
                    
                    if cancel_frac == whole_frac and cancel_frac != 1:
                        fracs.append([cancel_num, cancel_den])
                        print("Whole:", numstr + "/" + denstr, " Cancel:", str(cancel_num) + "/" + str(cancel_den), " Total:", whole_frac)
                        
numprod = 1
denprod = 1

for f in fracs:
    numprod *= f[0]
    denprod *= f[1]

print("Numprod:", numprod)
print("Denprod:", denprod)
print("Denominator (lowest):", denprod/numprod)
