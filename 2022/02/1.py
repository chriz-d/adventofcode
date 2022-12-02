lines = []
with open("input.txt") as file:
    lines = file.readlines()

opponentScores = {"A": 1, "B": 2, "C": 3}
playerScores = {"X": 1, "Y": 2, "Z": 3}
totalscore = 0

for line in lines:
    line = line.strip().split(" ")
    oppMove = line[0]
    playerMove = line[1]
    winner = ((3 + opponentScores[oppMove] - playerScores[playerMove]) % 3)
    if winner == 2:
        totalscore += 6 + playerScores[playerMove]
    elif winner == 0:
        totalscore += 3 + playerScores[playerMove]
    else:
        totalscore += playerScores[playerMove]
print(totalscore)