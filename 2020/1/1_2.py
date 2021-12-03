test_values = [1721, 979, 366, 299, 675, 1456]
real_values = []
REQ_VAL = 2020

with open("input.txt") as f:
    real_values = f.readlines()

real_values = [int(x.strip()) for x in real_values]

for e in real_values:
    for f in real_values:
        for g in real_values:
            if(e + f + g == REQ_VAL):
                print("%d + %d + %d = 2020" % (e, f, g))
                print("%d * %d * %d = %d" % (e, f, g, e*f*g))


