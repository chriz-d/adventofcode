grid = []
with open("input.txt") as file:
    grid = [x.strip('\n') for x in file.readlines()]

def getScenicScore(grid, x, y):
    # Top
    scoreTop = 0
    scoreBot = 0
    scoreLeft = 0
    scoreRight = 0
    for i in range(y-1, -1, -1):
        scoreTop += 1
        if int(grid[y][x]) <= int(grid[i][x]):
            break;
    # Bottom
    for i in range(y+1, len(grid)):
        scoreBot += 1
        if int(grid[y][x]) <= int(grid[i][x]):
            break;
    # Left
    for i in range(x-1, -1, -1):
        scoreLeft += 1
        if int(grid[y][x]) <= int(grid[y][i]):
            break;
    # Right
    for i in range(x+1, len(grid[y])):
        scoreRight += 1
        if int(grid[y][x]) <= int(grid[y][i]):
            break;

    return scoreTop * scoreBot * scoreLeft * scoreRight

scenicScores = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        scenicScores.append(getScenicScore(grid, x, y))

print(max(scenicScores))