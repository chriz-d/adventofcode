grid = []
with open("input.txt") as file:
    grid = [x.strip('\n') for x in file.readlines()]

def isVisible(grid, x, y):
    if y == 0 or y == len(grid)-1 or x == 0 or x == len(grid[x])-1:
        return True
    isVisibleTop = True
    isVisibleBot = True
    isVisibleLeft = True
    isVisibleRight = True
    # Top
    for i in range(y-1, -1, -1):
        if int(grid[y][x]) <= int(grid[i][x]):
            isVisibleTop = False
            break;
    # Bottom
    for i in range(y+1, len(grid)):
        if int(grid[y][x]) <= int(grid[i][x]):
            isVisibleBot = False
            break;
    # Left
    for i in range(x-1, -1, -1):
        if int(grid[y][x]) <= int(grid[y][i]):
            isVisibleLeft = False
            break;
    # Right
    for i in range(x+1, len(grid[y])):
        if int(grid[y][x]) <= int(grid[y][i]):
            isVisibleRight = False
            break;
    return isVisibleTop or isVisibleBot or isVisibleLeft or isVisibleRight
    
visibleCounter = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if isVisible(grid, x, y):
            visibleCounter += 1
print(visibleCounter)
