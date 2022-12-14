lines = []
with open("input.txt") as file:
    lines = [x.strip('\n') for x in file.readlines()]

# Parse input and get min and max value for offsetting
xMinVal = 999999
xMaxVal = 0
yMaxVal = 0
coordinateList = []
for line in lines:
    coordinateList.append([])
    coordinates = line.split(" -> ")
    for coordinateStr in coordinates:
        coordinate = [int(x) for x in coordinateStr.split(',')]
        coordinateList[-1].append(coordinate)
        if xMinVal > coordinate[0]:
            xMinVal = coordinate[0]
        if xMaxVal < coordinate[0]:
            xMaxVal = coordinate[0]
        if yMaxVal < coordinate[1]:
            yMaxVal = coordinate[1]

# Increase grid size so we have a run off area for sand
# Instead of checking ideal possible size of array, just make it big enough so the sand never gets out of bounds lol
xMinVal -= 170
xMaxVal += 170
yMaxVal += 2

# Create grid and draw cave walls
grid = []
for _ in range(yMaxVal + 1):
    grid.append(['.'] * (xMaxVal - xMinVal + 1))
for line in coordinateList:
    for i in range(len(line) - 1):
        start = line[i]
        end = line[i+1]
        xStart = min(line[i][0], line[i+1][0]) - xMinVal
        xEnd = max(line[i][0], line[i+1][0])  - xMinVal
        yStart = min(line[i][1], line[i+1][1])
        yEnd = max(line[i][1], line[i+1][1])
        for j in range(xStart, xEnd+1):
            grid[start[1]][j] = '#'
        for j in range(yStart, yEnd+1):
            grid[j][start[0] - xMinVal] = '#'
# Insert ground
grid[-1] = ['#'] * len(grid[-1])

# Simulate sand because it's coarse, rough, irritating, and it gets everywhere
sandCnt = 0
while True:
    falling = True
    sandPos = (500 - xMinVal, 0)
    while falling:
        # print(sandCnt)
        if grid[sandPos[1]][sandPos[0]] == '+':
            break
        if grid[sandPos[1]+1][sandPos[0]] == '.':
            sandPos = (sandPos[0], sandPos[1]+1)
        elif grid[sandPos[1]+1][sandPos[0]-1] == '.':
            sandPos = (sandPos[0]-1, sandPos[1]+1)
        elif grid[sandPos[1]+1][sandPos[0]+1] == '.':
            sandPos = (sandPos[0]+1, sandPos[1]+1)
        else:
            falling = False
            grid[sandPos[1]][sandPos[0]] = '+'
            sandCnt += 1
    if falling:
        break

print(sandCnt)