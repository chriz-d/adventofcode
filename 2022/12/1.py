lines = []
with open("input.txt") as file:
    lines = [x.strip('\n') for x in file.readlines()]

startPos = (0, 0)
endPos = (0, 0)
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == 'S':
            startPos = (x, y)
            lines[y] = lines[y].replace('S', 'a')
        elif lines[y][x] == 'E':
            endPos = (x, y)
            lines[y] = lines[y].replace('E', 'z')


visited = []
queue = [startPos]
distances = {startPos : 0}
while queue:
    pos = queue.pop(0)
    visited.append(pos)
    x = pos[0]
    y = pos[1]
    if x - 1 >= 0 and ord(lines[y][x]) - ord(lines[y][x-1]) >= -1 and (x-1, y) not in visited and (x-1, y) not in queue:
        queue.append((x-1, y))
        distances[(x-1, y)] = distances[(x, y)] + 1
    if y - 1 >= 0 and ord(lines[y][x]) - ord(lines[y-1][x]) >= -1 and (x, y-1) not in visited  and (x, y-1) not in queue:
        queue.append((x, y-1))
        distances[(x, y-1)] = distances[(x, y)] + 1
    if x + 1 < len(lines[y]) and ord(lines[y][x]) - ord(lines[y][x+1]) >= -1 and (x+1, y) not in visited  and (x+1, y) not in queue:
        queue.append((x+1, y))
        distances[(x+1, y)] = distances[(x, y)] + 1
    if y + 1 < len(lines) and ord(lines[y][x]) - ord(lines[y+1][x]) >= -1 and (x, y+1) not in visited  and (x, y+1) not in queue:
        queue.append((x, y+1))
        distances[(x, y+1)] = distances[(x, y)] + 1
print(distances[endPos])