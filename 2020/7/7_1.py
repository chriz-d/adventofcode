import re
with open("input.txt") as f:
    rules = f.readlines()

def findGold(bags, temp_list=[]):
    length = len(bags)
    for bag in bags:
        for line in rules:
            if bag in line[4:]:
                temp_list.append(line.split(" bags")[0])
                rules.remove(line)
    bags = temp_list
    if length != len(bags):
        findGold(bags)
        return len(bags)


print(findGold(["shiny gold"]))
