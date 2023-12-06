import re

def first():
    lengths = []
    records = []
    with open("input.txt") as f:
        lines = f.read().split("\n")
        lengths = [int(x) for x in re.findall("\d+", lines[0])]
        records = [int(x) for x in re.findall("\d+", lines[1])]

    product = 1
    for length, record in zip(lengths, records):
        win = []
        for i in range(length):
            distance = i * (length - i)
            if distance > record:
                win.append(distance)
        product *= len(win)
    print(product)
        
def second():
    length = 0
    record = 0
    with open("input.txt") as f:
        lines = re.sub(" ", "", f.read()).split("\n")
        lengths = [int(x) for x in re.findall("\d+", lines[0])]
        records = [int(x) for x in re.findall("\d+", lines[1])]

    product = 1
    for length, record in zip(lengths, records):
        win = []
        for i in range(length):
            distance = i * (length - i)
            if distance > record:
                win.append(distance)
        product *= len(win)
    print(product)

first()
second()