import math

units_dict = {0: '', 1: 'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
tens_dict = {0: '', 1: 'ten', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

def checkHundreds(num):
    print(units_dict[num] + "hundred" + "and")
    return len(units_dict[num] + "hundred" + "and")
    
def checkTens(num):
    print(tens_dict[num])
    return len(tens_dict[num])
    
def checkUnits(num):
    print(units_dict[num])
    return len(units_dict[num])

thousands = len("onethousand")
hundreds = 0
tens = 0
units = 0

for x in range(1, 1000):
    u = 0
    t = 0
    h = 0
    if 1 <= x < 10:
        u = x
        units += checkUnits(u)
    if 10 <= x < 100:
        t = x//10
        u = x%10
        tens += checkTens(t)
        units += checkUnits(u)
    if 100 <= x < 1000:
        h = x//100
        t = x//10%10
        u = x%10
        hundreds += checkHundreds(h)
        tens += checkTens(t)
        units += checkUnits(u)
        
    
    print(h, t, u)
    
print(thousands+hundreds+tens+units)
