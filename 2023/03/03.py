import re

def first(lines):
    part_number_sum = 0
    # Add padding
    lines.insert(0, "." * len(lines[0]))
    lines.append("." * len(lines[0]))
    for i, line in enumerate(lines):
        lines[i] = "." + lines[i] + "."
    
    # Find numbers
    matches_list = []
    for line in lines:
        matches_list.append(re.finditer("\d+", line))
    # Iterate and find adjacent symbols
    for y, match_line in enumerate(matches_list):
        for match in match_line:
            if any([has_adjacent_symbol(lines, x, y) for x in range(match.start(), match.end())]):
                part_number_sum += int(match.group())

    print(part_number_sum)

def second(lines):
    gear_ratio_sum = 0
    # Add padding
    lines.insert(0, "." * len(lines[0]))
    lines.append("." * len(lines[0]))
    for i, line in enumerate(lines):
        lines[i] = "." + lines[i] + "."
    
    gears = {}
    # Find numbers
    matches_list = []
    for line in lines:
        matches_list.append(re.finditer("\d+", line))
    # Iterate and find adjacent symbols
    for y, match_line in enumerate(matches_list):
        for match in match_line:
            if any([has_adjacent_symbol(lines, x, y) for x in range(match.start(), match.end())]):
                part_number_sum += int(match.group())



def has_adjacent_symbol(lines, x, y):
    for i in range(x - 1, x + 2):
        if lines[y-1][i] != "." and not lines[y-1][i].isdigit():
            return True
    for i in range(x - 1, x + 2):
        if lines[y+1][i] != "." and not lines[y+1][i].isdigit():
            return True
    if lines[y][x-1] != "." and not lines[y][x-1].isdigit():
        return True
    if lines[y][x+1] != "." and not lines[y][x+1].isdigit():
        return True
    return False
    
def get_adjacent_numbers(lines, x, y):


def get_indices(line, pos):
    start = pos
    end = pos
    while line[start-1].isdigit():
        start -= 1
    while line[end+1].isdigit():
        end += 1
    return start, end

lines = []
with open("input.txt") as f:
    lines = f.read().split("\n")
first(lines)
second(lines)