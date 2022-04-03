def dict_inc(value, dict, count):
    if value in dict:
        dict[value]+=count
    else:
        dict[value]=count

file = open('./input.txt', 'r')
line = file.readline().strip()
file.readline().strip()
first, last =line[0],line[-1]

seq={}
for i in range(len(line)-1):
    dict_inc(line[i:i+2], seq, 1)

patterns={}
line = file.readline().strip()
while line:
    patterns[line[:2]]=(line[0]+line[6],line[6]+line[1])
    line=file.readline().strip()

temp={}
for i in range(40):
    for j in seq:
        if j in patterns:
            dict_inc(patterns[j][0], temp, seq[j])
            dict_inc(patterns[j][1], temp, seq[j])
        else:
            temp[j]=seq[j]
    seq=temp
    temp={}

element={}
for i in seq:
    dict_inc(i[0], element, seq[i])
    dict_inc(i[1], element, seq[i])
    
element[first]+=1
element[last]+=1

print((max(element.values())-min(element.values()))/2)
