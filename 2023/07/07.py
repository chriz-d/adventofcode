import functools

ranks = {"penta": 20, "quad": 19, "fullhouse": 18, "triple": 17, "doubledouble": 16, "double": 15, "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

def eval_hand(hand):
    card_counts = {}
    for char in hand:
        if not char in card_counts:
            card_counts[char] = 0
        card_counts[char] += 1
    sorted_card_counts = sorted(card_counts.items(), key=lambda x: x[1])
    sorted_card_counts.reverse()
    if sorted_card_counts[0][1] == 5:
        return "penta"
    elif sorted_card_counts[0][1] == 4:
        return "quad"
    elif sorted_card_counts[0][1] == 3 and sorted_card_counts[1][1] == 2:
        return "fullhouse"
    elif sorted_card_counts[0][1] == 3:
        return "triple"
    elif sorted_card_counts[0][1] == 2 and sorted_card_counts[1][1] == 2:
        return "doubledouble"
    elif sorted_card_counts[0][1] == 2:
        return "double"
    else:
        return sorted(hand, key=lambda x: ranks[x])[0]

def handsorter(handA, handB):
    handA_val = eval_hand(handA)
    handB_val = eval_hand(handB)

    if handA_val == handB_val:
        for cardA, cardB in zip(handA, handB):
            if ranks[cardA] == ranks[cardB]:
                continue
            elif ranks[cardA] < ranks[cardB]:
                return 1
            elif ranks[cardA] > ranks[cardB]:
                return -1
    if ranks[handA_val] < ranks[handB_val]:
        return 1
    else:
        return -1

with open("example.txt") as f:
    games = f.read().split("\n")

hands = []
bets = {}
for game in games:
    hand, bet = game.split(" ")
    hands.append(hand)
    bets[hand] = bet

hands = sorted(hands, key=functools.cmp_to_key(handsorter))
hands.reverse()
multi = 0
for i, hand in enumerate(hands):
    multi += int(bets[hand]) * (i+1)
print(multi)