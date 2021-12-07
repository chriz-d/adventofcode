import math

positions = []
with open("input.txt") as file:
    positions = [int(x) for x in file.readline().split(',')]
# Part 1
leastFuelCost = 9999999
for i in range(max(positions)):
    fuelCost = 0
    for pos in positions:
        fuelCost += abs(pos - i)
    if fuelCost < leastFuelCost:
        leastFuelCost = fuelCost
print(leastFuelCost)

# Part 2 
leastFuelCost = 9999999999
for i in range(max(positions)):
    fuelCost = 0
    for pos in positions:
        fuelCost += math.comb(abs(pos - i) + 1, 2)
    if fuelCost < leastFuelCost:
        leastFuelCost = fuelCost
print(leastFuelCost)