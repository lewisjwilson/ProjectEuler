# Question
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


# Solution - iterate over number 1-1000, travsering dictionaries

import math

units_dict = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
              5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
tens_dict = {0: '', 1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty',
             5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
teens_dict = {0: '', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen',
              5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}
hundreds_list = [100, 200, 300, 400, 500, 600, 700, 800, 900]


def checkHundreds(num, and_switch):
    global string
    print(num)
    if and_switch:
        string += units_dict[num] + "hundred" + "and"
        return len(units_dict[num] + "hundred" + "and")
    else:
        string += units_dict[num] + "hundred"
        return len(units_dict[num] + "hundred")


def checkTens(num):
    global string
    string += tens_dict[num]
    return len(tens_dict[num])


def checkUnits(num):
    global string
    string += units_dict[num]
    return len(units_dict[num])


thousands = len("onethousand")
hundreds = 0
tens = 0
units = 0

string = ""

for x in range(1, 1000):
    u = 0
    t = 0
    h = 0
    if 1 <= x < 10:
        u = x
        units += checkUnits(u)
    if 10 <= x < 100:
        t = x//10
        u = x % 10
        if t == 1 and u != 0:
            string += teens_dict[u]
            tens += len(teens_dict[u])
        else:
            tens += checkTens(t)
            units += checkUnits(u)
    if 100 <= x < 1000:
        h = x//100
        t = x//10 % 10
        u = x % 10
        if x in hundreds_list:
            hundreds += checkHundreds(h, False)
        else:
            hundreds += checkHundreds(h, True)
        if t == 1 and u != 0:
            string += teens_dict[u]
            tens += len(teens_dict[u])
        else:
            tens += checkTens(t)
            units += checkUnits(u)
    print(string)
    print(h, t, u)
    string = ""

print(thousands+hundreds+tens+units)
