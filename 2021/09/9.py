# This is the just the crudest and over engineered solution possible. Please spare me.

lines = []
with open("testinput.txt") as file:
    lines = [x.strip('\n') for x in file.readlines()]
for i in range(len(lines)):
    lines[i] = [int(x) for x in str(lines[i])]

# Searches for the lowest given point using recursion
def isLowPoint(x, y):
    neighbors = []
    if (y - 1) >= 0 and (0 <= x or x < len(lines)):
        neighbors.append(lines[y - 1][x])
    if (y + 1) < len(lines) and (0 <= x or x < len(lines)):
        neighbors.append(lines[y + 1][x])
    if (x - 1) >= 0 and (0 <= y or y < len(lines)):
        neighbors.append(lines[y][x - 1])
    if (0 <= y or y < len(lines)) and (x + 1) < len(lines[y]):
        neighbors.append(lines[y][x + 1])
    return lines[y][x] < min(neighbors)

lowPointList = []
# Iterate over all fields and invoke recursion
for j in range(len(lines)):
    for i in range(len(lines[j])):
        if isLowPoint(i, j):
            lowPointList.append((i, j))

# All low points found, calculate risk level
sum = 0
for lowPoint in lowPointList:
    sum += lines[lowPoint[1]][lowPoint[0]] + 1
print(sum)

# Part 2
def flood(visited, x, y):
    if (x, y) in visited or lines[y][x] == 9:
        return
    else:
        visited.append((x,y))
    if (y - 1) >= 0:
        flood(visited, x, y - 1)
    if (y + 1) < len(lines):
        flood(visited, x, y + 1)
    if (x - 1) >= 0:
        flood(visited, x - 1, y)
    if (x + 1) < len(lines[y]):
        flood(visited, x + 1, y)
    
basinList = []
# Iterate over previous found low points and start depth search from there
for lowPoint in lowPointList:
    visited = []
    flood(visited, lowPoint[0], lowPoint[1])
    basinList.append(visited)

# calculate basin sizes and sort list to get top 3
basinList = sorted(basinList, key=len)
print(len(basinList[-1]) * len(basinList[-2]) * len(basinList[-3]))
