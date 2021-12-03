with open("input.txt") as f:
    map = f.readlines()

map = [x.strip("\n") for x in map]

rightSlopes = [1, 3, 5, 7, 1]
downSlopes =  [1, 1, 1, 1, 2]

totalTreeCount = 1
for i in range(len(rightSlopes)):
    x = 0
    y = 0
    treeCount = 0
    while(y < len(map)):
        if(map[y][x] == "#"):
            treeCount += 1
        x = (x + rightSlopes[i]) % len(map[y])
        y += downSlopes[i]
    totalTreeCount *= treeCount
print(totalTreeCount)