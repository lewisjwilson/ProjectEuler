# Question

# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


# Solution - Dynamic Programming

from array import *

def generate_table(coins, target, print_table):
    # Initializing coins and table
    coins.insert(0, 0)
    coin_idx = 0
    rows = len(coins)
    cols = target + 1
    
    table = [[0 for i in range(cols)] for j in range(rows)] 
    
    for row in range(rows):
        current_coin = coins[coin_idx]
        for col in range(cols):
          
            val = 0
            
            # Left value is always 1
            if(col == 0):
                val = 1
            elif(row == 0):
                val = 0
            elif(current_coin > col):
                val = table[row-1][col]
            else:
                val = table[row-1][col] + table[row][col-current_coin]
                
            table[row][col] = val
                
        coin_idx += 1
    
    if(print_table):
        # Printing
        coin_idx = 0
        for row in table:
            print(coins[coin_idx], row)
            coin_idx += 1
    
    return table[rows-1][cols-1]

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = generate_table(coins, target, False)
print(f"There are {ways} ways to create the a total of '{target}' using the coins {coins[1:]}!")
