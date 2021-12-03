lines = []
with open("input.txt") as file:
    lines = file.readlines()

horiz = 0
depth = 0
for line in lines:
    if "forward" in line:
        horiz += int(line[-2])
    elif "down" in line:
        depth += int(line[-2])
    elif "up" in line:
        depth -= int(line[-2])
print(horiz * depth)

horiz = 0
depth = 0
aim = 0
for line in lines:
    if "forward" in line:
        horiz += int(line[-2])
        depth += aim * int(line[-2])
    elif "down" in line:
        aim += int(line[-2])
    elif "up" in line:
        aim -= int(line[-2])
print(horiz * depth)
