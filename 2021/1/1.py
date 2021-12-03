lines = []
with open("input.txt") as file:
    lines = file.readlines()

def countIncreases(data):
    lastDepth = int(data[0])
    increaseCount = 0
    for line in data:
        if int(line) > lastDepth:
            increaseCount += 1
        lastDepth = int(line)
    print(increaseCount)

smoothedLines = []
for i in range(1, len(lines) - 1):
    smoothedLines.append(int(lines[i-1]) + int(lines[i]) + int(lines[i+1]))

countIncreases(lines)
countIncreases(smoothedLines)
