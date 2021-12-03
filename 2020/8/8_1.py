with open("input.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

acc = 0
visited = []
i = 0
running = True
while(running):
    if(i in visited):
        running = False
    else:
        visited.append(i)
        operator = lines[i].split(" ")[0]
        value = int(lines[i].split(" ")[1])
        if(operator == "acc"):
            acc += value
        elif(operator == "jmp"):
            i += (value-1)
        i += 1
print(acc)