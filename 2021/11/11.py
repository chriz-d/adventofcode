lines = []
with open("input.txt") as file:
    lines = [x.strip('\n') for x in file.readlines()]
for i in range(len(lines)):
    lines[i] = [int(x) for x in str(lines[i])]

def flash(x, y):
    lines[y][x] += 1
    if lines[y][x] > 9 and (x, y) not in flashed:
        flashed.append((x, y))
        if (y - 1) >= 0 and (x - 1) >= 0:
            flash(x - 1, y - 1)
        if (y < len(lines) - 1 and (x < len(lines[y]) - 1)):
            flash(x + 1, y + 1)
        if ((y - 1) >= 0) and (x < len(lines[y]) - 1):
            flash(x + 1, y - 1)
        if (y < len(lines) - 1) and ((x - 1) >= 0):
            flash(x - 1, y + 1)
        if (y - 1) >= 0:
            flash(x, y - 1)
        if (y + 1) < len(lines):
            flash(x, y + 1)
        if (x - 1) >= 0:
            flash(x - 1, y)
        if (x + 1) < len(lines[y]):
            flash(x + 1, y)

steps = 300
flashCount = 0
for i in range(steps):
    onlyFlash = True
    flashed = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            lines[y][x] += 1
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] > 9:
                flash(x, y)
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] > 9:
                lines[y][x] = 0
                flashCount += 1
            else:
                onlyFlash = False
    if onlyFlash:
        print("Only flashes at step: ", i+1)
print(flashCount)