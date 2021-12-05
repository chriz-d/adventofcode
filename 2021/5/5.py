# read input
lines = []
with open("input.txt") as file:
    lines = file.readlines()

# parse input
start = []
end = []
for line in lines:
    temp = line.split("->")
    start.append(temp[0].strip().split(','))
    end.append(temp[1].strip().split(','))

# convert list to int
for elem in start:
    elem[0] = int(elem[0])
    elem[1] = int(elem[1])
for elem in end:
    elem[0] = int(elem[0])
    elem[1] = int(elem[1])

# create empty 2d list
field = []
for i in range(1000):
    field.append([])
    for j in range(1000):
        field[i].append(0)

# start "drawing" lines in 2d array
for i in range(len(start)):
    # if start[i][0] == end[i][0]:
    #     if start[i][1] < end[i][1]:
    #         for y in range(start[i][1], end[i][1] + 1, 1):
    #             field[y][start[i][0]] += 1
    #     else:
    #         for y in range(start[i][1], end[i][1] - 1, -1):
    #             field[y][start[i][0]] += 1
    # elif start[i][1] == end[i][1]:
    #     if start[i][0] < end[i][0]:
    #         for x in range(start[i][0], end[i][0] + 1, 1 ):
    #             field[start[i][1]][x] += 1
    #     else:
    #         for x in range(start[i][0], end[i][0] - 1, -1):
    #             field[start[i][1]][x] += 1

    # this is the same as the top commented out part
    if (start[i][0] == end[i][0]) or (start[i][1] == end[i][1]): # check if line is actually horizontal or vertical
        for y in range(start[i][1], end[i][1] + (1 if start[i][1] < end[i][1] else -1), 1 if start[i][1] < end[i][1] else -1):
            for x in range(start[i][0], end[i][0] + (1 if start[i][0] < end[i][0] else -1), 1 if start[i][0] < end[i][0] else -1):
                field[y][x] += 1
    else: # diagonal
        stepX = 0
        stepY = 0
        x = start[i][0] - end[i][0]
        y = start[i][1] - end[i][1]
        if x < 0 and y < 0:
            stepX = 1
            stepY = 1
        elif x > 0 and y > 0:
            stepX = -1
            stepY = -1
        elif x > 0 and y < 0:
            stepX = -1
            stepY = 1
        elif x < 0 and y > 0:
            stepX = 1
            stepY = -1
        cursor = start[i].copy()
        while cursor != end[i]:
            field[cursor[1]][cursor[0]] += 1
            cursor[0] += stepX
            cursor[1] += stepY
        field[cursor[1]][cursor[0]] += 1
        
# count fields >1
sum = 0
for x in range(len(field)):
    for y in range(len(field[x])):
        if field[x][y] > 1:
            sum += 1
print(sum)
