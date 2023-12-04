import re

def first(cards):
    pile_worth = 0
    for card in cards:
        multi = 0
        winning_numbers, actual_numbers = parseLine(card)
        matches = len(set(winning_numbers) & set(actual_numbers))
        pile_worth += (2 ** (matches - 1)) if matches > 0 else 0
    print(pile_worth)

def second(cards):
    card_cnt = 0
    memory = {}
    for i, card in enumerate(cards):
        card_cnt += 1
        winning_numbers, actual_numbers = parseLine(card)
        matches = len(set(winning_numbers) & set(actual_numbers))
        for j in range(1, matches + 1):
            card_cnt += processCard(i + j, memory)
    print(card_cnt)

def processCard(card_nr, memory):
    card_cnt = 1
    if card_nr in memory:
        return memory[card_nr]
    winning_numbers, actual_numbers = parseLine(cards[card_nr])
    matches = len(set(winning_numbers) & set(actual_numbers))
    for j in range(1, matches + 1):
        card_cnt += processCard(card_nr + j, memory)
    memory[card_nr] = card_cnt
    return card_cnt

def parseLine(card):
    winning_numbers, actual_numbers = card.split("|")
    winning_numbers = [int(x) for x in re.findall("\d+", winning_numbers)]
    actual_numbers = [int(x) for x in re.findall("\d+", actual_numbers)]
    return winning_numbers, actual_numbers

cards = []
with open("input.txt") as f:
    cards = [x.split(":")[1] for x in f.readlines()]

first(cards)
second(cards)