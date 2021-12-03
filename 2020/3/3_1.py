with open("input.txt") as f:
    map = f.readlines()

map = [x.strip("\n") for x in map]

x = 0
y = 0
treeCount = 0
while(y < len(map)):
    if(map[y][x] == "#"):
        treeCount += 1
    x = (x + 3) % len(map[y])
    y += 1
print(treeCount)