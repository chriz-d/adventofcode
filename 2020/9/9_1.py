with open("input.txt") as f:
    numbers = f.readlines()

numbers = [x.strip() for x in numbers]
numbers = [int(x) for x in numbers]

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
        print(number)
    found = False
    i += 1