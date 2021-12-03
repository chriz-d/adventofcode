with open("input.txt") as f:
    lines = f.readlines()

lines = [x.strip("\n") for x in lines]

sum = 0
questionSetList = []
for line in lines:
    if(line != ""):
        questionSet = set()
        for character in line:
            questionSet.add(character)
        questionSetList.append(questionSet)
    else:
        sum += len(set.intersection(*questionSetList))
        questionSetList = []
sum += len(set.intersection(*questionSetList))
print(sum)