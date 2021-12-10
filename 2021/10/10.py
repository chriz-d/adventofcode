lines = []
with open("input.txt") as file:
    lines = [x.strip('\n') for x in file.readlines()]

matching = {')' : '(', ']' : '[', '}' : '{', '>' : '<'}
matching2 = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}
syntaxScoreTable = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
autoCompleteScoreTable = {')' : 1, ']' : 2, '}' : 3, '>' : 4}

syntaxScore = 0
autoCompleteScoreList = []
for line in lines:
    stack = []
    for i in range(len(line)):
        if line[i] in matching2.keys():
            stack.append(line[i])
        elif matching[line[i]] == stack[-1]:
            stack.pop()
        else:
            syntaxScore += syntaxScoreTable[line[i]]
            break
        if i == (len(line) - 1):
            autoCompleteScore = 0
            while stack:
                autoCompleteScore *= 5
                autoCompleteScore += autoCompleteScoreTable[matching2[stack.pop()]]
            autoCompleteScoreList.append(autoCompleteScore)
autoCompleteScoreList.sort()
print(syntaxScore)
print(autoCompleteScoreList[int(len(autoCompleteScoreList) / 2)])