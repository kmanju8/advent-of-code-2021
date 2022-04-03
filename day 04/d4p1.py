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

print("first board to complete is:",1+lastturns.index(min(lastturns)),"on turn:", min(lastturns))

# and then work out score of board 43 by hand haha. or the janky way below

board = [95, 18, 69, 85, 63,16, 78, 97, 10, 41,53, 98, 73, 87, 19,15, 35, 94, 57, 82,48, 40, 14,  3, 38]

total=0
final=0
for i in board:
    if position[str(i)]>29:
        total+=i
    elif position[str(i)]==29:
        final=i
    
print(total*final)
