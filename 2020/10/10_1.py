with open("input.txt") as f:
    adapters = f.readlines()

adapters = [x.strip() for x in adapters]
adapters = [int(x) for x in adapters]

adapters.sort()
currentAdapter = 0
oneJoltCount = 0
threeJoltCount = 0
for adapter in adapters:
    if(adapter - currentAdapter == 1):
        oneJoltCount += 1
    elif(adapter - currentAdapter == 3):
        threeJoltCount += 1
    currentAdapter = adapter
threeJoltCount += 1 # device adapter
print(oneJoltCount * threeJoltCount)