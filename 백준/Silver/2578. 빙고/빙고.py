bingo_board = [list(map(int, input().split())) for _ in range(5)]
call_numbers = [int(x) for _ in range(5) for x in input().split()]

checked = [[False]*5 for _ in range(5)]

pos = {}
for i in range(5):
    for j in range(5):
        pos[bingo_board[i][j]] = (i, j)

def count_bingo():
    count = 0
    for i in range(5):
        if all(checked[i][j] for j in range(5)):
            count += 1

    for j in range(5):
        if all(checked[i][j] for i in range(5)):
            count += 1

    if all(checked[i][i] for i in range(5)):
        count += 1
    
    if all(checked[i][4-i] for i in range(5)):
        count += 1

    return count

for idx, number in enumerate(call_numbers, start=1):
    if number in pos:
        x, y = pos[number]
        checked[x][y] = True
        if count_bingo() >= 3:
            print(idx)
            break