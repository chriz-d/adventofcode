import math

commands = []
with open("input.txt") as file:
    commands = [x.strip('\n') for x in file.readlines()]

def getDistance(p1, p2):
    p1p2 = (p2[0] - p1[0], p2[1] - p1[1])
    return math.sqrt(p1p2[0] * p1p2[0] + p1p2[1] * p1p2[1])

tailpos = (0, 0)
oldHeadPos = (0, 0)
headpos = (0, 0)
allTailPos = set([(0, 0)])
for command in commands:
    direction, amount = command.split(" ")
    for _ in range(int(amount)):
        oldHeadPos = headpos
        if direction == 'R':
            headpos = (headpos[0] + 1, headpos[1])
        elif direction == 'L':
            headpos = (headpos[0] - 1, headpos[1])
        elif direction == 'U':
            headpos = (headpos[0], headpos[1] - 1)
        elif direction == 'D':
            headpos = (headpos[0], headpos[1] + 1)

        if getDistance(headpos, tailpos) > 1.5:
            tailpos = oldHeadPos
            allTailPos.add(tailpos)

print(len(allTailPos))