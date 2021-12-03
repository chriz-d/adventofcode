with open("input.txt") as f:
    passports = f.readlines()

passports = [x.strip("\n") for x in passports]
fieldCount = 0
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
validPassports = 0
for line in passports:
    if(line == ""):
        if(fieldCount == len(fields)):
            validPassports += 1
        fieldCount = 0
    for field in fields:
        if(field in line):
            fieldCount += 1
if(fieldCount == len(fields)):
    validPassports += 1
print(validPassports)
    
