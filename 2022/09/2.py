import math

commands = []
with open("input.txt") as file:
    commands = [x.strip('\n') for x in file.readlines()]

def getDistance(p1, p2):
    p1p2 = (p2[0] - p1[0], p2[1] - p1[1])
    return math.sqrt(p1p2[0] * p1p2[0] + p1p2[1] * p1p2[1])

rope = []
for _ in range(2):
    rope.append((0, 0))

allTailPos = set([(0, 0)])
for command in commands:
    direction, amount = command.split(" ")
    for _ in range(int(amount)):
        oldHeadPos = rope[0]
        if direction == 'R':
            rope[0] = (rope[0][0] + 1, rope[0][1])
        elif direction == 'L':
            rope[0] = (rope[0][0] - 1, rope[0][1])
        elif direction == 'U':
            rope[0] = (rope[0][0], rope[0][1] - 1)
        elif direction == 'D':
            rope[0] = (rope[0][0], rope[0][1] + 1)

        if getDistance(rope[0], rope[-1]) > 1.5:
            rope[-1] = oldHeadPos
            allTailPos.add(rope[-1])

print(len(allTailPos))