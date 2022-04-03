values={")":("(",3), "]":("[",57), "}":("{",1197), ">":("<",25137) }
total=0

file = open('./input.txt', 'r')
line = file.readline().strip()
while line:
    stack=[]
    for i in line:
        if i in ("(","[","{","<"):
            stack.append(i)
            continue
        else:
            if stack.pop() != values[i][0]:
                total += values[i][1]
                break

    line = file.readline().strip()

print(total)
