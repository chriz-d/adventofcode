with open("input.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

validPwCount = 0
for e in lines:
    splitString = e.split(":")
    pw = splitString[1].strip()
    tmp = splitString[0].split(" ")
    reqChar = tmp[1]
    rangeOfChar = tmp[0].split("-")
    charCounter = 0
    for char in pw:
        if(char == reqChar):
            charCounter += 1
    if(int(rangeOfChar[0]) <= charCounter <= int(rangeOfChar[1])):
        validPwCount += 1
print(validPwCount)