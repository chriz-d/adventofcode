import re

def first(lines):
    calib_sum = 0
    for line in lines:
        digits = re.findall("\d", line)
        if digits:
            calib_sum += int(digits[0] + digits[-1])
    print(calib_sum)

def second(lines):
    calib_sum = 0
    number_words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight" : "8", "nine": "9"}
    for line in lines:
        matches = re.finditer('(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        digits = [match.group(1) for match in matches]
        first = digits[0]
        last = digits[-1]
        if len(first) > 1:
            first = number_words[first]
        if len(last) > 1:
            last = number_words[last]
        calib_sum += int(first + last)
    print(calib_sum)

lines = []
with open("input.txt") as f:
    lines = f.read().split("\n")
first(lines)
second(lines)