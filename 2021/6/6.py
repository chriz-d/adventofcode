ages = []
with open("input.txt") as file:
    ages = file.readlines()[0].split(',')
ages = [int(x) for x in ages]

jellyCount = [0] * 9
for age in ages:
    jellyCount[age] += 1
for day in range(256):
    tmp = jellyCount[0]
    for i in range(8):
        jellyCount[i] = jellyCount[i+1]
    jellyCount[8] = tmp
    jellyCount[6] += tmp
print(sum(jellyCount))
