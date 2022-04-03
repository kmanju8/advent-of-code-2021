"""identical to last part, but use mean instead of median

last part we were optimising (minimizing) sum of (positions-alignment point) which is linear.

here, we are minimizing sum of a quadratic (triangular numbers): 
essentially minimizing standard deviation.
if you understand the idea behind the standard deviation formula, 
you can realise as close to the mean as possible is the best position
"""

def triangle(n):
    return (n*(n+1))/2

pos = [int(i) for i in open('input.txt', 'r').readline().split(",")]
pos.sort()

mean = [int(sum(pos)/len(pos))-i for i in range(-1,2)]

print(min([sum([triangle(abs(i-m)) for i in pos]) for m in mean]))