with open("example.txt") as f:
    adapters = f.readlines()

adapters = [x.strip() for x in adapters]
adapters = [int(x) for x in adapters]

adapters.sort()
currentAdapter = 0
oneJoltCount = 0
threeJoltCount = 0
countList = []
for i in range(len(adapters)):
    countList.append(0)
for i in range(len(adapters)):
    if(adapters[i] + 1 in adapters):
        countList[i] += 1
    if(adapters[i] + 2 in adapters):
        countList[i] += 1
    if(adapters[i] + 3 in adapters):
        countList[i] += 1
result = 1
for count in countList:
    if count != 0:
        result *= count
print(result)