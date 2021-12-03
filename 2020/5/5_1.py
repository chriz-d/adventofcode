with open("input.txt") as f:
    boardingPasses = f.readlines()
boardingPasses = [x.strip("\n") for x in boardingPasses]

def getSeat(line):
    row = line[0:7]
    column = line[8:10]
    row = row.replace("B", "1")
    row = row.replace("F", "0")
    row = int(row, 2)
    column = column.replace("R", "1")
    column = column.replace("L", "0")
    column = int(column, 2)
    return (row, column)

highestID = 0
for boardingPass in boardingPasses:
    seat = getSeat(boardingPass)
    seatID = seat[0] * 8 + seat[1]
    if(highestID < seatID):
        highestID = seatID
print(highestID)