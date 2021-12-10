import numpy as np

def checkWin(board):
    # check rows
    for row in board:
        if row.count(-1) == 5:
            # bingo
            return True
    # check columns
    transposed = np.array(board).T.tolist() # numpy whyever converts the -1 to a string
    for row in transposed:
        if row.count("-1") == 5:
            # bingo
            return True
    return False

def calculateScore(board, draw):
    sum = 0
    for row in board:
        for number in row:
            if number != -1:
                sum += int(number)
    sum *= int(draw)
    return sum

def parseInput(filename):
    # read file
    lines = []
    with open(filename) as file:
        lines = file.readlines()
    # Parse input
    draws = lines[0]
    draws = draws.strip('\n')
    draws = draws.split(',')

    # get boards
    boards = []
    i = -1
    for line in lines[1:]:
        if line == '\n':
            boards.append([])
            i += 1
        else:
            line = line.strip('\n')
            boards[i].append(line.split(' '))
    # cleanup parsed content
    for board in boards:
        for row in board:
            while('' in row):
                row.remove('')
            while('\n' in row):
                row.remove('\n')
    return draws, boards

def playBingo(draws, boards):
    # Iterate over
    winners = []
    for draw in draws:
        for board in boards:
            for row in board:
                for i in range(len(row)):
                    if draw == row[i]:
                        row[i] = -1
            if checkWin(board):
                print("Next winner", calculateScore(board, draw))
                winners.append(board)
        if len(winners) != 0:
            for winner in winners:
                boards.remove(winner)
            winners.clear()

draws, boards = parseInput("input.txt")
playBingo(draws, boards)