lines = ""
with open("input.txt") as file:
    lines = [x.strip('\n') for x in file.readlines()]

stream = lines[0]
queue = []
for i in range(len(stream)):
    queue.append(stream[i])
    if len(queue) >= 4:
        if len(queue) == len(set(queue)):
            print(i+1)
            break
        queue.pop(0)

