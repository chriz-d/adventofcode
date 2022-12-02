lines = []
with open("input.txt") as file:
    lines = file.readlines()

playerScores = {"X": 1, "Y": 2, "Z": 3}
win = {"A": "Y", "B": "Z", "C": "X"}
loose = {"A": "Z", "B": "X", "C": "Y"}
draw = {"A": "X", "B": "Y", "C": "Z"}
totalscore = 0

for line in lines:
    line = line.strip().split(" ")
    oppMove = line[0]
    result = line[1]
    if result == "Z":
        totalscore += 6 + playerScores[win[oppMove]]
    elif result == "Y":
        totalscore += 3 + playerScores[draw[oppMove]]
    else:
        totalscore += playerScores[loose[oppMove]]
print(totalscore)