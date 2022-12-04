pairs = []
with open("input.txt") as file:
    pairs = [x.strip('\n').split(",") for x in file.readlines()]

def getRangeFromString(string):
    rangeStartEnd = string.split("-")
    return set(range(int(rangeStartEnd[0]), int(rangeStartEnd[1]) + 1))

overlapCnt = 0
for pair in pairs:
    firstRange = getRangeFromString(pair[0])
    secondRange = getRangeFromString(pair[1])
    for elem in firstRange:
        if elem in secondRange:
            overlapCnt += 1
            break
print(overlapCnt)

