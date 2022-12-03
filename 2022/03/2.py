backpacks = []
with open("input.txt") as file:
    backpacks = [x.strip('\n') for x in file.readlines()]

prioSum = 0

for i in range(0, len(backpacks), 3):
    for item in backpacks[i]:
        if item in backpacks[i+1] and item in backpacks[i+2]:
            prioSum += ord(item) - 96 if item.islower() else ord(item) - 38
            break
print(prioSum)