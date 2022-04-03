DAYS = 256

file = open('input.txt', 'r')
line = [int(i) for i in file.readline().split(",")]
count={key: 0 for (key) in range(7)}
for i in line:
    count[i]+=1

baby=[0,0]

for i in range(DAYS):
    count[(i+2)%7]+=(count[i%7]-baby[1])    
    baby[0],baby[1]=(count[i%7]-baby[1]),baby[0]

total=0
for i in count:
    total+=count[i]

print(total)