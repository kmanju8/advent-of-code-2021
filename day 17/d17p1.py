# target area: x=70..125, y=-159..-121
# very brute forced. Only y coord matters for part 1

# this loop brute forces to find best initial y velocity, using a reasonable range of values.
valid=[]
for i in range(100,1000):
    y = 0
    dy = i
    while True:
        y += dy
        dy -= 1

        # if x>=70 and x<=125:
        if y>=-159 and y<=-121:
            valid.append(i)

        if y <-159:
            break

# this loop finds max height
y = 0
dy = max(valid)
heights=[]
while True:
    heights.append(y)
    y += dy
    dy -= 1

    # if x>=70 and x<=125:
    if y<0:
        break

print(max(heights))