backpacks = []
with open("input.txt") as file:
    backpacks = [x.strip('\n') for x in file.readlines()]

prioSum = 0

for backpack in backpacks:
    for item in backpack[:len(backpack) // 2]:
        if item in backpack[(len(backpack)  // 2):]:
            prioSum += ord(item) - 96 if item.islower() else ord(item) - 38
            break
print(prioSum)