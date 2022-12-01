lines = []
with open("input.txt") as file:
    lines = file.readlines()

currElve = 0
elves = [0]
for line in lines:
    if line != "\n":
        elves[-1] += int(line)
    else:
        elves.append(0)
elves.sort()

print(elves[-1] + elves[-2] + elves[-3])
