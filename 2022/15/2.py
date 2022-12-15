import re

sensors = []
with open("example.txt") as file:
    sensors = [x.strip('\n') for x in file.readlines()]

def getManhattanDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Map over Maps, Y-Values are keys and values are maps, which map X-values to width values of the beacon on that line
filledYValues = {}

for sensor in sensors:
    positions = re.findall(r'-?\d+', sensor)
    sensorPos = (int(positions[0]), int(positions[1]))
    beaconPos = (int(positions[2]), int(positions[3]))
    distance = getManhattanDistance(sensorPos, beaconPos)
    # Lower half
    for i in range(sensorPos[1], sensorPos[1]+distance):
        if i not in filledYValues:
            filledYValues[i] = {}
        filledYValues[i][sensorPos[0]] = distance - i + sensorPos[1]
    # Upper half
    for i in range(sensorPos[1], sensorPos[1]-distance, -1):
        if i not in filledYValues:
            filledYValues[i] = {}
        filledYValues[i][sensorPos[0]] = distance + i - sensorPos[1]
    print("Sensor done.")

y = 10
line = set([])
print(filledYValues[y])
for x in filledYValues[y]:
    width = filledYValues[y][x]
    for i in range(x, x+width+1):
        line.add(i)
    for i in range(x, x-width-1, -1):
        line.add(i)
print(len(line)-1) # Solution is somehow off by one

for y in range(20):
    for x in range(20):
        if y not in filledYValues:
            continue
        isOutside = True
        for xVal in filledYValues[y]:
            minVal = xVal - filledYValues[y][xVal]
            maxVal = xVal + filledYValues[y][xVal]
            if not (minVal < x and x < maxVal):
                isOutside = isOutside and True
            else:
                isOutside = isOutside and False
        if isOutside:
            print("%d, %d" % (x, y))