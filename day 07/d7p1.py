"""the median of locations is where fuel consumption is minimized.
at the median, half of the points are before, and half after.

it's worth considering the rate of change of fuel usage at this point:
it's 0 (or as close as possible). as we are summing the diffs between median and points
moving one unit forward means that the fuel consumption for all the points before the point increases,
but it decreases for every point after (and vice versa)"""

pos = [int(i) for i in open('input.txt', 'r').readline().split(",")]
pos.sort()

# find median of positions. also find value before and after median as failsafe for non-integer stuff.
mid = [pos[int(len(pos)/2)+i] for i in range(3)]

# calculate total fuel usage for above points, take min.
print(min([sum([abs(i-m) for i in pos]) for m in mid]))
