lines = ""
with open("input.txt") as file:
    lines = [x.strip('\n') for x in file.readlines()]

def getDirectorySize(lines, dir):
    # listingStart = lines.index("$ cd " + dir) # Doesnt work, dir with same name deeper in hierarchy can appear
    # Instead watch out for nested folders potential same name
    listingStart = 0
    nestedLvl = 0
    # Iterate through lines until cd command with wanted directory is found
    while lines[listingStart] != "$ cd " + dir or nestedLvl != 0:
        if "$ cd .." in lines[listingStart]:
            nestedLvl -= 1
        elif "$ cd " in lines[listingStart]:
            nestedLvl += 1
        listingStart += 1
    dirSize = 0
    i = listingStart + 2 # Skip cd and ls command
    # Add all sizes together and if another dir is found use recursion
    while i < len(lines) and "$ cd " not in lines[i]:
        firstWord, secondWord = lines[i].split(' ')
        if firstWord == "dir":
            dirSize += getDirectorySize(lines[i:], secondWord)
        else:
            dirSize += int(firstWord)
        i += 1
    print("Size of %s %d" % (dir, dirSize))
    return dirSize

dirsum = 0
totalSpace = 70000000
neededSpace = 30000000
usedSpace = getDirectorySize(lines, '/')
unusedSpace = totalSpace - usedSpace
deletionCandidateSizes = []
for i in range(len(lines)):
    if "dir" in lines[i]:
        dirSize = getDirectorySize(lines[i:], lines[i].split(' ')[1])
        if (unusedSpace + dirSize) >= neededSpace:
            deletionCandidateSizes.append(dirSize)

print(min(deletionCandidateSizes))