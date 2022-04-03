values={"(":1, "[":2, "{":3, "<":4}
reverse={")":"(", "]":"[", "}":"{", ">":"<"}
scores=[]

file = open('./input.txt', 'r')
line = file.readline().strip()
while line:
    broken=False
    stack=[]
    
    for i in line:
        if i in values:
            stack.append(i)
        elif stack.pop() != reverse[i]:
            broken=True
            break
    
    # string is broken not incomplete so skip it
    if broken:
        line = file.readline().strip()
        continue

    stack.reverse()
    total = 0
    for i in stack:
        total= 5*total + values[i]
    scores.append(total)

    line = file.readline().strip()

scores.sort()
print(scores[int(len(scores)/2)])
