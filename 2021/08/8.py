lines = []
with open("input.txt") as file:
    lines = file.readlines()

uniqueNumList = []
fourDigitValList = []

for line in lines:
    uniqueNumList.append(line.split('|')[0].strip().split(' '))
    fourDigitValList.append(line.split('|')[1].strip().split(' '))
# Part 1
sum = 0
for val in fourDigitValList:
    for entry in val:
        # print(len(entry))
        if (len(entry) == 2) or (len(entry) == 4) or (len(entry) == 3) or (len(entry) == 7):
            sum += 1
print(sum)

# Part 2
sum = 0
for i in range(len(uniqueNumList)):
    # Locations of codes correspond to resembling number
    digitMapping = [-1] * 10
    # Map the easy ones first
    for j in range(len(uniqueNumList[i])):
        if len(uniqueNumList[i][j]) == 2:
            digitMapping[1] = uniqueNumList[i][j]
        elif len(uniqueNumList[i][j]) == 3:
            digitMapping[7] = uniqueNumList[i][j]
        elif len(uniqueNumList[i][j]) == 4:
            digitMapping[4] = uniqueNumList[i][j]
        elif len(uniqueNumList[i][j]) == 7:
            digitMapping[8] = uniqueNumList[i][j]
    # Map the harder ones by deduction
    while -1 in digitMapping:
        for j in range(len(uniqueNumList[i])):
            if uniqueNumList[i][j] in digitMapping:
                continue
            if len(uniqueNumList[i][j]) == 6 and all([x in uniqueNumList[i][j] for x in digitMapping[4]]): # Search for 9
                digitMapping[9] = uniqueNumList[i][j]
            elif len(uniqueNumList[i][j]) == 6 and digitMapping[7] != -1 and all([x in uniqueNumList[i][j] for x in digitMapping[7]]) and digitMapping[9] != 0: # Search for 0
                digitMapping[0] = uniqueNumList[i][j]
            elif len(uniqueNumList[i][j]) == 6 and digitMapping[0] != -1 and digitMapping[9] != -1: # Search for 6
                digitMapping[6] = uniqueNumList[i][j]
            elif len(uniqueNumList[i][j]) == 5 and digitMapping[1] != -1 and all([x in uniqueNumList[i][j] for x in digitMapping[1]]): # Search for 3
                digitMapping[3] = uniqueNumList[i][j]
            elif len(uniqueNumList[i][j]) == 5 and digitMapping[6] != -1 and all([x in digitMapping[6] for x in uniqueNumList[i][j]]): # Search for 5
                digitMapping[5] = uniqueNumList[i][j]
            elif digitMapping.count(-1) == 1: # Search for 2
                digitMapping[2] = uniqueNumList[i][j]
    # Sort the codes because order is random in input
    for j in range(len(digitMapping)):
        digitMapping[j] = sorted(digitMapping[j])
    value = ""
    # Finally append found digits
    for digit in fourDigitValList[i]:
        value += str(digitMapping.index(sorted(digit)))
    sum += int(value)
print(sum)