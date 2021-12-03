with open("input.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

validPwCount = 0
for e in lines:
    splitString = e.split(":")
    pw = splitString[1].strip()
    tmp = splitString[0].split(" ")
    reqChar = tmp[1]
    posIndices = tmp[0].split("-")
    if((pw[int(posIndices[0])-1] == reqChar) ^ (pw[int(posIndices[1])-1] == reqChar)):
        validPwCount += 1
print(validPwCount)