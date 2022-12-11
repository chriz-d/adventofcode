lines = []
with open("input.txt") as file:
    lines = [x.strip('\n') for x in file.readlines()]

class Monkey:
    def __init__(self, items, operation, operator, divisor, trueMonkey, falseMonkey):
        self.items = items
        self.divisor = divisor
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.operation = operation
        self.operator = operator
        self.inspectCnt = 0
    
    def evaluateItem(self, item):
        self.inspectCnt += 1
        if self.operation == '+':
            if self.operator == "old":
                item = item + item
            else:
                item = item + self.operator
        elif self.operation == '*':
            if self.operator == "old":
                item = item * item
            else:
                item = item * self.operator
        item = item // 3
        return item

    def getThrownIndex(self, item):
        if item % self.divisor == 0:
            return self.trueMonkey
        else:
            return self.falseMonkey
        

monkeys = []
for i in range(len(lines)):
    if "Monkey" not in lines[i]:
        continue
    items = [int(x) for x in lines[i+1][lines[i+1].index(':')+1:].split(', ')]
    operation = '+' if '+' in lines[i+2] else '*'
    operator = "old" if lines[i+2].count("old") == 2 else int(lines[i+2][-2:].strip(' '))
    divisor = int(lines[i+3].split("by ")[1])
    trueMonkey = int(lines[i+4][-1])
    falseMonkey = int(lines[i+5][-1])

    monkeys.append(Monkey(items, operation, operator, divisor, trueMonkey, falseMonkey))

for i in range(20):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.pop(0)
            item = monkey.evaluateItem(item)
            nextMonkey = monkeys[monkey.getThrownIndex(item)]
            nextMonkey.items.append(item)

inspectCntList = []
for monkey in monkeys:
    inspectCntList.append(monkey.inspectCnt)
first = max(inspectCntList)
inspectCntList.remove(first)
second = max(inspectCntList)
print(first * second)