import re

lines = []
with open("input.txt") as file:
    lines = [x.strip('\n') for x in file.readlines()]

# Find split between visualization and instructions
x = 0
while lines[x] != "":
    x += 1

vis = lines[:x]
instructions = lines[x+1:]
STACK_OFFSET = 4

def getStack(idx, vis):
    idx -= 1 # pretend first stack starts at index 0
    stack = []
    row = len(vis) - 2 # Ignore numbers of stacks
    column = idx * STACK_OFFSET + 1
    while vis[row][column] != " " and row >= 0:
        stack.append(vis[row][column])
        row -= 1
    return stack

def getStacks(vis):
    stackNumbering = len(vis) - 1
    stackCount = max([int(x) for x in vis[stackNumbering].split("  ")])
    stacks = []
    for i in range(1, stackCount + 1):
        stacks.append(getStack(i, vis))
    return stacks

def moveStack(origin, destination):
    destination.append(origin.pop())

stacks = getStacks(vis)
for instruction in instructions:
    amount, originIdx, destinationIdx = [int(x) for x in re.findall(r'\d+', instruction)]
    for i in range(amount):
        moveStack(stacks[originIdx - 1], stacks[destinationIdx - 1])
result = ""
for stack in stacks:
    result += stack[-1]
print(result)