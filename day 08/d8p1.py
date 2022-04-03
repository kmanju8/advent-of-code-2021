file = open('./input.txt', 'r')

total = 0

line = file.readline().strip()
while line:
    out = line[line.index("|")+1:].split()
    total += len([x for x in out if (len(x)!=5 and len(x)!=6)])

    line = file.readline().strip()

print(total)
