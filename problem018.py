# A* Algorithm - https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

tri = [[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,4,82,47,65],
[19,1,23,75,3,34],
[88,2,77,73,7,63,67],
[99,65,4,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

def check_fscore(open_nodes):
    highest_cost = 0
    value = 0
    idx = 0
    for item in open_nodes:
        g = 0 + item
        h = len(tri) - item
        f = g + h
        if f > highest_cost:
            highest_cost = f
            value = item
        idx += 1
    return [value, highest_cost]
    
max_val = 0 # maximum ESTIMATED distance between first and end node (most likely higher)
for x in range(len(tri)):
    max_val += max(tri[x])
print("Maximum Possible Value:", max_val)

f = 0 # total cost of the node (f = h + g)
g = 0 # distance between start node and current node
h = 0 # heuristic (estimated distance from current to end node)

open_nodes = []
closed_nodes = []
open_nodes.append(tri[0][0])

[value, fscore] = check_fscore(open_nodes)
print("Open:",open_nodes,"Closed:",closed_nodes)
closed_nodes.append(value)
open_nodes.pop(open_nodes.index(value))

print("Value in open_nodes:",value)
print("F-score:", fscore)

print("Open:",open_nodes,"Closed:",closed_nodes)
