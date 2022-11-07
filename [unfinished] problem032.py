from itertools import permutations

#testing
print("Need to utilise 9 number spaces.")
print("\nMin 2x2 nums (12x23):", 12*23)
print("Max 2x2 nums (98x76):", 98*76)
print("Min: 7, Max 8 - 2x2 Not Applicable.")
print("\nMin 2x3 nums (12x345):", 12*345)
print("Max 2x3 nums (98x765):", 98*765)
print("Min: 9, Max 10 - 2x3 Somewhat Applicable.")
print("\nMin 3x2 nums (123x45):", 123*45)
print("Max 2x3 nums (987x65):", 987*65)
print("Min: 9, Max 10 - 3x2 Somewhat Applicable.")
print("\nMin 3x3 nums (123x456):", 123*456)
print("Min: 11 - 3x3 Not Applicable.")

# patterns must either be of the form 2x3 or 3x2

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
perms = list(permutations(nums))
results = set()

for perm in perms:
    two = int(perm[0] + perm[1])
    three = int(perm[2] + perm[3] + perm[4])
    res = int(perm[5] + perm[6] + perm[7] + perm[8])
    if two * three == res:
        #if res not in results:
        results.add(res)
        print(two, "x", three, "=", res)
        
    three = int(perm[0] + perm[1] + perm[2])
    two = int(perm[3] + perm[4])
    res = int(perm[5] + perm[6] + perm[7] + perm[8])
    if two * three == res:
        #if res not in results:
        results.add(res)
        print(two, "x", three, "=", res)
            
print(sum(results))
