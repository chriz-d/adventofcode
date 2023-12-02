import re

def first(games):
    dice = {"red": 12,"green": 13, "blue": 14}
    possible_game_sum = 0
    for i, game in enumerate(games):
        hands = game[8:].split(";")
        viable = True
        j = 0
        while viable and j < len(hands):
            digits = re.finditer("\d+", hands[j])
            colors = re.finditer("blue|red|green", hands[j])
            for digit, color in zip(digits, colors):
                if int(digit.group()) > dice[color.group()]:
                    viable = False
                    break
            j += 1
        if viable:
            possible_game_sum += i+1
        viable = True
    print(possible_game_sum)

def second(games):
    dice = {"red": 12,"green": 13, "blue": 14}
    cube_power_sum = 0
    for i, game in enumerate(games):
        dices = game[8:]
        hands = dices.split(";")
        min_cubes = {"blue": 0, "red": 0, "green": 0}
        for hand in hands:
            digits = re.finditer("\d+", hand)
            colors = re.finditer("blue|red|green", hand)
            for digit, color in zip(digits, colors):
                digit = int(digit.group())
                color = color.group()
                if digit > min_cubes[color]:
                    min_cubes[color] = digit
        cube_power_sum += min_cubes["blue"] * min_cubes["red"] * min_cubes["green"]
    print(cube_power_sum)


games = []
with open("input.txt") as f:
    games = f.read().split("\n")
first(games)
second(games)