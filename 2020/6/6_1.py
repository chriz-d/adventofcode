with open("input.txt") as f:
    lines = f.readlines()

lines = [x.strip("\n") for x in lines]

sum = 0
questionList = []
for line in lines:
    for character in line:
        if(character not in questionList):
            questionList.append(character)
    if(line == ""):
        sum += len(questionList)
        questionList = []
sum += len(questionList)
print(sum)