file = open('./input.txt', 'r')
line = file.readline().strip()
file.readline().strip()
call = line.split(",")

lastturns = []

position={}
for i in range(len(call)):
    position[call[i]] = i

for x in range(100):
    board = []
    for i in range(5):
        board.append(file.readline().strip().split())
    file.readline().strip()

    # calculate what turn board is complete
    completeturns=[]
    for i in range(5):
        completeturns.append(max([position[j] for j in board[i]]))
        completeturns.append(max([position[j] for j in [row[i] for row in board]]))
    lastturns.append(min(completeturns))

file.close()

print("last board to complete is:",1+lastturns.index(max(lastturns)),"on turn:", max(lastturns))

# and then work out score of board 84 by hand haha. or the janky way below

board = [19, 27, 96, 54, 36,33, 32, 65, 11, 26, 0, 47, 25, 59, 56,41, 45, 76, 14, 98,52, 22, 31, 66, 38]

total=0
final=0
for i in board:
    if position[str(i)]>85:
        total+=i
    elif position[str(i)]==85:
        final=i
    
print(total*final)
