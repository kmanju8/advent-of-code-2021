data = [i[:-1] for i in open('input.txt')]

# gamma and delta are symmetric so I mixed them up probably but it doesn't matter
gamma = 0
for i in range(12):
    
    count = 0
    for j in data:
        if j[i]=="1":
            count += 1
        else:
            count -= 1
            
    if count > 0:
        gamma = gamma << 1
        gamma += 1
    else:
        gamma = gamma << 1
    
print(((2**12) - (1+gamma))*gamma)