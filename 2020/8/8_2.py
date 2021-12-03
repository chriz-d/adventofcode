with open("input.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

def isLoop():
    acc = 0
    visited = []
    i = 0
    running = True
    while(running):
        if(i in visited):
            running = False
        else:
            if(i == len(lines)):
                print(acc)
                return False
            visited.append(i)
            operator = lines[i].split(" ")[0]
            value = int(lines[i].split(" ")[1])
            if(operator == "acc"):
                acc += value
            elif(operator == "jmp"):
                i += (value-1)
            i += 1
    return True
    
for j in range(0, len(lines)):
    operator = lines[j].split(" ")[0]
    if(operator == "jmp"):
        lines[j] = lines[j].replace("jmp", "nop")
        if(not isLoop()):
            break
        lines[j] = lines[j].replace("nop", "jmp")
    elif(operator == "nop"):
        lines[j] = lines[j].replace("nop", "jmp")
        if(not isLoop()):
            break
        lines[j] = lines[j].replace("jmp", "nop")