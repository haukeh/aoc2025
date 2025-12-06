inp = [l.strip() for l in open("input/03.txt").readlines()]

p1 = 0
for row in inp: 
    j = 0
    for i, c in enumerate(row):
        for ii in range(i + 1, len(row)):
            jj = int(c + row[ii])
            if jj > j: 
                j = jj
    p1 += j

print(p1)