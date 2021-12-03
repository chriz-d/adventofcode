lines = []
with open("input.txt") as file:
    lines = file.readlines()
lines = [line.strip("\n") for line in lines]
gamma = ""
epsilon = ""

transposed = [''.join(i) for i in zip(*lines)]
for i in range(len(transposed)):
    zeroes = sum(['0' == char for char in transposed[i]])
    ones = len(lines) - zeroes
    if zeroes < ones:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
print(int(gamma, 2) * int(epsilon, 2))

oxyList = lines.copy()
coList = lines.copy()
for i in range(len(transposed)):
    transposed = [''.join(i) for i in zip(*oxyList)]
    zeroes = sum(['0' == char for char in transposed[i]])
    ones = len(oxyList) - zeroes
    toDel = []
    if len(oxyList) != 1:
        if zeroes <= ones:
            for line in oxyList:
                if line[i] == '0':
                    toDel.append(line)
            for entry in toDel:
                oxyList.remove(entry)
        elif zeroes > ones:
            for line in oxyList:
                if line[i] == '1':
                    toDel.append(line)
            for entry in toDel:
                oxyList.remove(entry)
for i in range(len(transposed)):
    transposed = [''.join(i) for i in zip(*coList)]
    zeroes = sum(['0' == char for char in transposed[i]])
    ones = len(coList) - zeroes
    toDel = []
    if len(coList) != 1:
        if zeroes <= ones:
            for line in coList:
                if line[i] == '1':
                    toDel.append(line)
            for entry in toDel:
                coList.remove(entry)
        elif zeroes > ones:
            for line in coList:
                if line[i] == '0':
                    toDel.append(line)
            for entry in toDel:
                coList.remove(entry)
print(int(oxyList[0], 2) * int(coList[0], 2))

