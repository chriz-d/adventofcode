lines = []
with open("input.txt") as file:
    lines = [x.strip('\n') for x in file.readlines()]

x = 1
clkCnt = 0
prgCnt = 0
isBusy = False
signalStrengths = []
while prgCnt < len(lines):
    clkCnt += 1
    if (clkCnt - 20) % 40 == 0:
        signalStrengths.append(clkCnt * x)
    if lines[prgCnt] == "noop":
        prgCnt += 1
    else:
        _, val = lines[prgCnt].split(" ")
        if isBusy:
            x += int(val)
            isBusy = False
            prgCnt += 1 
        else:
            isBusy = True
    

print(sum(signalStrengths))