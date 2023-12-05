import re

def first():
    category_strings = []
    with open("input.txt") as f:
        category_strings = f.read().split("\n\n")
    seeds = [int(x) for x in re.findall("\d+", category_strings.pop(0))]
    isDone = [False] * len(seeds)
    for category_string in category_strings:
        ranges = category_string.split("\n")
        ranges.pop(0)
        for rangee in ranges:
            dest_range, src_range, size = [int(x) for x in rangee.split(" ")]
            for i, seed in enumerate(seeds):
                if src_range <= seed <= (src_range + size - 1) and not isDone[i]:
                    seeds[i] = dest_range + abs(src_range - seed)
                    isDone[i] = True
        isDone = [False] * len(seeds)
    print(min(seeds))

def second():
    with open("input.txt") as f:
        category_strings = f.read().split("\n\n")
    seeds = [int(x) for x in re.findall("\d+", category_strings.pop(0))]
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i] + seeds[i+1]))
    isDone = [False] * len(seeds)
    for category_string in category_strings:
        ranges = category_string.split("\n")
        ranges.pop(0)
        new_ranges = []
        for rangee in ranges:
            ranges_copy = list(seed_ranges)
            dest_range, src_range, size = [int(x) for x in rangee.split(" ")]
            for i, seed_range in enumerate(seed_ranges):
                seed_start = seed_range[0]
                seed_end = seed_range[1]
                src_start = src_range
                src_end = src_start + size
                dest_start = dest_range
                dest_end = dest_start + size
                if src_start < seed_start < src_end:
                    changed_range = (max(src_start, seed_start), min(seed_start, src_end))
                    new_ranges.append(changed_range)
                    
                if src_start < seed_end < src_end:
                    pass
                if src_range <= seed <= (src_range + size - 1) and not isDone[i]:
                    seeds[i] = dest_range + abs(src_range - seed)
                    isDone[i] = True
            seed_ranges = ranges_copy
        for 
        isDone = [False] * len(seeds)
    print(min(seeds))

first()
second()
        