import re

with open("input.txt") as f:
    passports = f.readlines()

passports = [x.strip("\n") for x in passports]
fieldCount = 0
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eyeColour = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
validPassports = 0
passport = {}
for line in passports:
    if(line == ""):
        fieldCount = 0
        if(len(passport) == len(fields)):
            if(1920 <= int(passport["byr"]) <= 2002):
                fieldCount += 1
            if(2010 <= int(passport["iyr"]) <= 2020):
                fieldCount += 1
            if(2020 <= int(passport["eyr"]) <= 2030):
                fieldCount += 1
            heightStr = passport["hgt"]
            if("cm" in heightStr and 150 <= int(heightStr.strip("cm")) <= 193):
                fieldCount += 1
            elif("in" in heightStr and 59 <= int(heightStr.strip("in")) <= 76):
                fieldCount += 1
            regexp = re.compile("^#[0-9a-f]{6}")
            if(regexp.search(passport["hcl"])):
                fieldCount += 1
            if(passport["ecl"] in eyeColour):
                fieldCount += 1
            regexp = re.compile("\d{9}$")
            if(regexp.search(passport["pid"])):
                fieldCount += 1
            if(fieldCount == len(fields)):
                validPassports += 1
        passport = {}
        continue
    passportFields = line.split(" ")
    for passportField in passportFields:
        fieldAndVal = passportField.split(":")
        if(fieldAndVal[0] != "cid"):
            passport[fieldAndVal[0]] = fieldAndVal[1]

print(validPassports)
