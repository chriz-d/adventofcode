with open("input.txt") as f:
    numbers = f.readlines()

numbers = [x.strip() for x in numbers]
numbers = [int(x) for x in numbers]

def getInvalidNumber():
    preAmbleSize = 25
    i = 0
    found = False
    for number in numbers[preAmbleSize:]:
        for preNumber in numbers[i:i+preAmbleSize]:
            for preNumber2 in numbers[i:i+preAmbleSize]:
                if(preNumber != preNumber2 and not found):
                    if((preNumber + preNumber2) == number):
                        found = True
        if(not found):
            return number
        found = False
        i += 1

def getSum(invalid):
    for i in range(0, len(numbers)):
        for j in range(i + 2, len(numbers)):
            window = numbers[i:j]
            if(sum(window) == invalid):
                return min(window) + max(window)

invalid = getInvalidNumber()
print(getSum(invalid))