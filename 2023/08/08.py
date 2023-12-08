import re
import math

with open("input.txt") as f:
    lines = f.read().split("\n")

def first(lines):
    turns = lines[0]
    nodesL = {}
    nodesR = {}
    for line in lines[2:]:
        start, left, right = re.findall("[A-Z]+", line)
        nodesL[start] = left
        nodesR[start] = right

    curr_node = "AAA"
    steps = 0
    while curr_node != "ZZZ":
        if turns[steps % len(turns)] == "L":
            curr_node = nodesL[curr_node]
        elif turns[steps % len(turns)] == "R":
            curr_node = nodesR[curr_node]
        steps += 1
    print(steps)

def second(lines):
    turns = lines[0]
    nodesL = {}
    nodesR = {}
    a_nodes = []
    for line in lines[2:]:
        start, left, right = re.findall("\d*[A-Z]+", line)
        nodesL[start] = left
        nodesR[start] = right
        if start[-1] == "A":
            a_nodes.append(start)

    steps = 0
    intervals = []
    while len(a_nodes) != 0:
        if turns[steps % len(turns)] == "L":
            for i, node in enumerate(a_nodes):
                a_nodes[i] = nodesL[node]
        elif turns[steps % len(turns)] == "R":
            for i, node in enumerate(a_nodes):
                a_nodes[i] = nodesR[node]
        steps += 1
        for node in list(a_nodes):
            if node[-1] == "Z":
                intervals.append(steps)
                a_nodes.remove(node)
    print(math.lcm(*intervals))

first(lines)
second(lines)