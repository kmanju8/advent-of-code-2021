# target area: x=70..125, y=-159..-121

# straightforward brute force within sensible ranges
valid=[]
for i in range(1,200):
    for j in range(-200,200):
        x = 0
        dx = i
        y = 0
        dy = j
        while True:
            x += dx
            dx += 1 if dx<0 else -1 if dx>0 else 0
            y += dy
            dy -= 1
            if x>=70 and x<=125:
                if y>=-159 and y<=-121:
                    valid.append((i,j))
                    break

            if x>125 or (x<70 and dx==0) or y <-159:
                break

print(len(valid))
