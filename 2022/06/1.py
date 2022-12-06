lines = ""
with open("input.txt") as file:
    lines = [x.strip('\n') for x in file.readlines()]

stream = lines[0]
windowSize = 4
for i in range(windowSize, len(stream)):
    if windowSize == len(set(stream[i-windowSize:i])):
        print(i)
        break